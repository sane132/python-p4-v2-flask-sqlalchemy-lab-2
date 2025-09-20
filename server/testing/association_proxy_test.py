from app import app, db
from server.models import Customer, Item, Review
import pytest

@pytest.fixture(autouse=True)
def setup_database():
    """Ensure fresh tables exist for each test."""
    with app.app_context():
        db.drop_all()
        db.create_all()
        yield
        db.session.remove()
        db.drop_all()


class TestAssociationProxy:
    '''Customer in models.py'''

    def test_has_association_proxy(self):
        '''has association proxy to items'''
        with app.app_context():
            c = Customer(name="Test Customer")
            i = Item(name="Test Item", price=10.0)

            db.session.add_all([c, i])
            db.session.commit()

            r = Review(comment='great!', customer=c, item=i)
            db.session.add(r)
            db.session.commit()

            assert hasattr(c, 'items')
            assert i in c.items
