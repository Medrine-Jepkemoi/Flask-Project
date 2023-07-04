from flask_sqlalchemy import SQLAlchemy
import datetime

db = SQLAlchemy()

# User table
class User(db.Model):
    __tablename__ = 'users'
    user_id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String, unique=True)
    password = db.Column(db.String)
    bought_properties = db.relationship('BoughtProperty', back_populates='user')
    ratings = db.relationship('Rating', back_populates='user')
    def __repr__(self):
        return f'User(user_id={self.user_id}, email={self.email})'
# Admin table
class Admin(db.Model):
    __tablename__ = 'admins'
    admin_id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String, unique=True)
    password = db.Column(db.String)
    properties = db.relationship('Property', back_populates='admin')
    def __repr__(self):
        return f'Admin(admin_id={self.admin_id}, email={self.email})'
# Property Category table
class PropertyCategory(db.Model):
    __tablename__ = 'property_categories'
    category_id = db.Column(db.Integer, primary_key=True)
    category_name = db.Column(db.String)
    properties = db.relationship('Property', back_populates='category')
    def __repr__(self):
        return f'PropertyCategory(category_id={self.category_id}, category_name={self.category_name})'
# Property table
class Property(db.Model):
    __tablename__ = 'properties'
    property_id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String)
    image = db.Column(db.String)
    description = db.Column(db.String)
    price = db.Column(db.Integer)
    is_rental = db.Column(db.Boolean)
    is_sold = db.Column(db.Boolean)
    category_id = db.Column(db.Integer, db.ForeignKey('property_categories.category_id'))
    admin_id = db.Column(db.Integer, db.ForeignKey('admins.admin_id'))
    admin = db.relationship('Admin', back_populates='properties')
    category = db.relationship('PropertyCategory', back_populates='properties')
    ratings = db.relationship('Rating', back_populates='property')
    def __repr__(self):
        return f'Property(property_id={self.property_id}, title={self.title}, description={self.description}, ' \
               f'price={self.price}, is_rental={self.is_rental}, is_sold={self.is_sold}, ' \
               f'category_id={self.category_id}, admin_id={self.admin_id})'
# Bought Property table
class BoughtProperty(db.Model):
    __tablename__ = 'bought_properties'
    bought_property_id = db.Column(db.Integer, primary_key=True)
    property_id = db.Column(db.Integer, db.ForeignKey('properties.property_id'))
    user_id = db.Column(db.Integer, db.ForeignKey('users.user_id'))
    purchase_date = db.Column(db.String, default=datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"))
    property = db.relationship('Property')
    user = db.relationship('User', back_populates='bought_properties')
    def __repr__(self):
        return f'BoughtProperty(bought_property_id={self.bought_property_id}, ' \
               f'property_id={self.property_id}, user_id={self.user_id}, purchase_date={self.purchase_date})'

# Rating table
class Rating(db.Model):
    __tablename__ = 'ratings'
    rating_id = db.Column(db.Integer, primary_key=True)
    property_id = db.Column(db.Integer, db.ForeignKey('properties.property_id'))
    user_id = db.Column(db.Integer, db.ForeignKey('users.user_id'))
    rating = db.Column(db.Integer)
    property = db.relationship('Property')
    user = db.relationship('User')
    def __repr__(self):
        return f'Rating(rating_id={self.rating_id}, property_id={self.property_id}, user_id={self.user_id}, ' \
               f'rating={self.rating})'