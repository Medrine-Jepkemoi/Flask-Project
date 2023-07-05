from flask_sqlalchemy import SQLAlchemy
from random import choice as rc
from faker import Faker
from models import *
from app import app

# Import your Flask app and initialize the SQLAlchemy extension
from app import app, db

# Import your models
from models import User, Admin, PropertyCategory, Property, BoughtProperty

# Create fake data
def create_fake_data():
    fake = Faker()

    User.query.delete()
    Admin.query.delete()
    PropertyCategory.query.delete()
    Property.query.delete()
    BoughtProperty.query.delete()

    # Create users
    users = []
    for _ in range(10):
        user = User(email=fake.email(), password=fake.password())
        users.append(user)

    # Create admins
    admins = []
    for _ in range(1):
        admin = Admin(email=fake.email(), password=fake.password())
        admins.append(admin)

    # Create property categories
    categories = []
    for _ in range(3):
        category = PropertyCategory(category_name=fake.word())
        categories.append(category)

    # Create properties
    properties = []
    images = ["../client/public/images/image1.jpg", "../client/public/images/image2.jpg", "../client/public/images/image3.jpg"]
    for _ in range(20):
        title = fake.word()
        description = fake.sentence()
        price = fake.random_int(min=10000, max=1000000)
        quantity = fake.random_int(min=100, max=1000)  # Include quantity attribute
        is_rental = fake.boolean()
        is_sold = fake.boolean()
        category = fake.random_element(elements=categories)
        admin = fake.random_element(elements=admins)
        property = Property(title=title, description=description, price=price, quantity=quantity,
                            is_rental=is_rental, is_sold=is_sold, category=category, admin=admin)
        properties.append(property)

    # Create bought properties
    bought_properties = []
    for _ in range(10):
        property = fake.random_element(elements=properties)
        user = fake.random_element(elements=users)
        purchase_date = fake.date_time_between(start_date='-1y', end_date='now')
        total_price = fake.random_int(min=100, max=1000) 
        bought_quantity = fake.random_int(min=100, max=1000)
        bought_property = BoughtProperty(property=property, user=user, purchase_date=purchase_date, total_price=total_price, bought_quantity=bought_quantity)
        bought_properties.append(bought_property)

    # Create ratings
    ratings = []
    for _ in range(10):
        property = fake.random_element(elements=properties)
        user = fake.random_element(elements=users)
        rating = fake.random_int(min=1, max=5)
        rating_entry = Rating(property=property, user=user, rating=rating)
        ratings.append(rating_entry)

    # Add the objects to the database session
    db.session.add_all(users)
    db.session.add_all(admins)
    db.session.add_all(categories)
    db.session.add_all(properties)
    db.session.add_all(bought_properties)
    db.session.add_all(ratings)

    # Commit the changes to the database
    db.session.commit()

# Seed the data
if __name__ == '__main__':
    with app.app_context():
        create_fake_data()
