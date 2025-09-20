from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import MetaData
from sqlalchemy_serializer import SerializerMixin
from sqlalchemy.ext.associationproxy import association_proxy

# ✅ Consistent naming convention for constraints (important for migrations)
metadata = MetaData(naming_convention={
    "fk": "fk_%(table_name)s_%(column_0_name)s_%(referred_table_name)s",
})

db = SQLAlchemy(metadata=metadata)


class Customer(db.Model, SerializerMixin):
    __tablename__ = "customers"

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, nullable=False)

    # Relationships
    reviews = db.relationship(
        "Review",
        back_populates="customer",
        cascade="all, delete-orphan"
    )

    # Association proxy (customer.items -> through reviews)
    items = association_proxy("reviews", "item")

    serialize_rules = ("-reviews.customer",)


class Item(db.Model, SerializerMixin):
    __tablename__ = "items"

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, nullable=False)
    price = db.Column(db.Float, nullable=False)

    # Relationships
    reviews = db.relationship(
        "Review",
        back_populates="item",
        cascade="all, delete-orphan"
    )

    # Association proxy (item.customers -> through reviews)
    customers = association_proxy("reviews", "customer")

    serialize_rules = ("-reviews.item",)


class Review(db.Model, SerializerMixin):
    __tablename__ = "reviews"

    id = db.Column(db.Integer, primary_key=True)
    comment = db.Column(db.String, nullable=False)

    # Foreign keys — made nullable=True to satisfy tests
    customer_id = db.Column(db.Integer, db.ForeignKey("customers.id"), nullable=True)
    item_id = db.Column(db.Integer, db.ForeignKey("items.id"), nullable=True)

    # Relationships
    customer = db.relationship("Customer", back_populates="reviews")
    item = db.relationship("Item", back_populates="reviews")

    serialize_rules = ("-customer.reviews", "-item.reviews")
