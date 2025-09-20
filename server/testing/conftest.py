#!/usr/bin/env python3
import pytest
from app import app, db

def pytest_itemcollected(item):
    """
    Customize how pytest displays collected test names.
    Uses the test class docstring and function docstring if available.
    """
    par = item.parent.obj
    node = item.obj
    pref = par.__doc__.strip() if par.__doc__ else par.__class__.__name__
    suf = node.__doc__.strip() if node.__doc__ else node.__name__
    if pref or suf:
        item._nodeid = ' '.join((pref, suf))


@pytest.fixture(autouse=True, scope="session")
def setup_database():
    """
    Automatically set up and tear down the database for tests.
    Runs once per test session.
    """
    with app.app_context():
        db.create_all()   # ✅ Create all tables before tests
        yield             # 🔄 Run the tests
        db.drop_all()     # 🧹 Clean up after tests
