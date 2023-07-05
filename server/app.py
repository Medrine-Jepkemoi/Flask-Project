from flask import Flask, request, make_response, jsonify, json
from datetime import datetime
from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy


from models import db, User, Admin, Property, PropertyCategory, BoughtProperty
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///app.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['JSONIFY_PRETTYPRINT_REGULAR'] = True

migrate = Migrate(app, db)

db.init_app(app)

# Index route
@app.route('/')
def index():
    return "Index for Nyumba Mali"

# API route to view all products
@app.route('/products', methods=['GET'])
def get_all_products():
    try:
        # Retrieve all products from the database
        products = Property.query.all()
        
        # Create a list to store product details
        products_list = []
        
        # Iterate through each product and extract relevant information
        for product in products:
            # Get the category name based on the category_id
            category = PropertyCategory.query.get(product.category_id)
            category_name = category.category_name if category else None
            
            product_data = {
                'property_id': product.property_id,
                'title': product.title,
                'image': product.image,
                'description': product.description,
                'price': product.price,
                'quantity': product.quantity,
                'is_rental': product.is_rental,
                'is_sold': product.is_sold,
                'category_name': category_name,  # Include the category name
            }
            products_list.append(product_data)
        
        # Return the list of products as a JSON response
        return jsonify(products_list), 200
    
    except Exception as e:
        # Return an error message if any exception occurs
        return jsonify({'error': str(e)}), 500


# API route to view products by category name
@app.route('/products/<category_name>', methods=['GET'])
def get_products_by_category(category_name):
    try:
        # Retrieve the category by name
        category = PropertyCategory.query.filter_by(category_name=category_name).first()

        if category:
            # Retrieve products based on the category_id
            products = Property.query.filter_by(category_id=category.category_id).all()

            # Create a list to store product details
            products_list = []

            # Iterate through each product and extract relevant information
            for product in products:
                product_data = {
                    'title': product.title,
                    'image': product.image,
                    'description': product.description,
                    'price': product.price,
                    'quantity': product.quantity,
                    'is_rental': product.is_rental,
                    'is_sold': product.is_sold,
                    'category_name': category_name,
                }
                products_list.append(product_data)

            # Return the list of products for the specified category as a JSON response
            return jsonify(products_list), 200
        else:
            # Return an error message if the category does not exist
            return jsonify({'error': f'Category "{category_name}" not found.'}), 404

    except Exception as e:
        # Return an error message if any exception occurs
        return jsonify({'error': str(e)}), 500
    

# User signup route
@app.route('/signup', methods=['GET', 'POST'])
def signup():

    if request.method == 'GET':
        existing_accounts = []

        users = User.query.all()

        for user in users:
            user_dict = user.to_dict()
            existing_accounts.append(user_dict)

        response = make_response(jsonify(existing_accounts), 200)

        return response
    
    elif request.method == 'POST':

        email = request.form.get("email")
        password = request.form.get("password")

        if not email or not password:
            response = make_response(jsonify({'error': 'Email and password are required.'}), 400)
            return response

        existing_user = User.query.filter_by(email=email).first()
        if existing_user:
            response = make_response(jsonify({'error': 'Email already exists. Please use a different email.'}), 400)
            return response

        new_acc = User(email=email, password=password)

        db.session.add(new_acc)
        db.session.commit()

        user_dict = new_acc.to_dict()

        response = make_response(
            jsonify(user_dict),
            201
        )

        return response


# User login route
@app.route('/login', methods=['POST'])
def login():
    email = request.form.get("email")
    password = request.form.get("password")

    if not email or not password:
        response = make_response(jsonify({'error': 'Email and password are required.'}), 400)
        return response

    user = User.query.filter_by(email=email).first()

    if not user:
        response = make_response(jsonify({'error': 'Invalid email or password.'}), 401)
        return response

    if user.password != password:
        response = make_response(jsonify({'error': 'Invalid email or password.'}), 401)
        return response

    # User login successful
    response = make_response(jsonify({'message': 'Login successful.'}), 200)
    return response



# Property purchase/rent route
@app.route('/property/purchase', methods=['POST'])
def purchase_property():
    user_id = request.form.get('user_id')
    title = request.form.get('title')
    quantity = request.form.get('quantity')
    option = request.form.get('option')

    if not user_id or not title or not quantity or not option:
        response = make_response(jsonify({'error': 'User ID, Title, Quantity, and Option are required.'}), 400)
        return response

    user = User.query.get(user_id)
    property = Property.query.filter_by(title=title).first()

    if not user or not property:
        response = make_response(jsonify({'error': 'Invalid User ID or Title.'}), 404)
        return response

    if property.is_sold:
        response = make_response(jsonify({'error': 'Property is already sold.'}), 400)
        return response

    if option == 'rent':
        # Perform rental logic here
        rental_price = property.price

        # Create a new BoughtProperty entry for rental
        bought_property = BoughtProperty(
            property_id=property.property_id,
            user_id=user_id,
            bought_quantity=quantity,
            rental_price=rental_price
        )

        db.session.add(bought_property)
        db.session.commit()

        response = make_response(jsonify({'message': 'Property rented successfully.'}), 200)
        return response

    elif option == 'buy':
        # Perform purchase logic here
        if property.quantity < int(quantity):
            response = make_response(jsonify({'error': 'Insufficient quantity available.'}), 400)
            return response

        total_price = property.price * int(quantity)

        # Create a new BoughtProperty entry for purchase
        bought_property = BoughtProperty(
            property_id=property.property_id,
            user_id=user_id,
            bought_quantity=quantity,
            total_price=total_price
        )

        property.quantity -= int(quantity)

        if property.quantity == 0:
            property.is_sold = True

        db.session.add(bought_property)
        db.session.commit()

        response = make_response(jsonify({'message': 'Property purchased successfully.'}), 200)
        return response

    else:
        response = make_response(jsonify({'error': 'Invalid option. Must be either "rent" or "buy".'}), 400)
        return response






if __name__ == '__main__':
    app.run(port=5555)