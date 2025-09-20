from app import app
from models import db, Customer, Item, Review

with app.app_context():
    print("Deleting existing data...")
    Review.query.delete()
    Customer.query.delete()
    Item.query.delete()
    
    print("Creating customers...")
    c1 = Customer(name='Tal Yuri')
    c2 = Customer(name='Jane Doe')
    c3 = Customer(name='John Smith')
    
    customers = [c1, c2, c3]
    db.session.add_all(customers)
    
    print("Creating items...")
    i1 = Item(name='Laptop Backpack', price=49.99)
    i2 = Item(name='Insulated Coffee Mug', price=9.99)
    i3 = Item(name='Wireless Mouse', price=19.99)
    i4 = Item(name='USB-C Hub', price=24.99)
    
    items = [i1, i2, i3, i4]
    db.session.add_all(items)
    
    print("Creating reviews...")
    r1 = Review(comment='Excellent quality and very comfortable!', customer=c1, item=i1)
    r2 = Review(comment='Keeps my coffee hot for hours!', customer=c1, item=i2)
    r3 = Review(comment='A great deal for the price.', customer=c2, item=i3)
    r4 = Review(comment='Love the ergonomic design.', customer=c3, item=i3)
    r5 = Review(comment='Exactly what I needed for my new laptop.', customer=c3, item=i4)
    
    reviews = [r1, r2, r3, r4, r5]
    db.session.add_all(reviews)
    db.session.commit()
    
    print("Seeding complete!")