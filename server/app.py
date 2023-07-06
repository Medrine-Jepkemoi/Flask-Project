from flask import Flask, request, make_response, jsonify, json
from datetime import date
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
@app.route('/user/products', methods=['GET'])
def get_all_products():
    products = Property.query.all()
        
    products_list = []
        
    for product in products:
        category = PropertyCategory.query.get(product.category_id)
        category_name = category.category_name if category else None
            
        product_data = {
            'property_id': product.property_id,
            'title': product.title,
            'image': product.image,
            'description': product.description,
            'price': product.price,
            'quantity': product.quantity,
            'category_name': category_name, 
        }
        products_list.append(product_data)

    response = make_response(jsonify(products_list), 200)   
    return response
    


# API route to view products by category name
@app.route('/user/products/<category_name>', methods=['GET'])
def get_products_by_category(category_name):
    
    category = PropertyCategory.query.filter_by(category_name=category_name).first()

    if category:
        products = Property.query.filter_by(category_id=category.category_id).all()

        products_list = []

        for product in products:
            product_data = {
                'title': product.title,
                'image': product.image,
                'description': product.description,
                'price': product.price,
                'quantity': product.quantity,
            }
            products_list.append(product_data)

        response = make_response(jsonify(products_list), 200)
        return response
    else:
        response = make_response(jsonify({'error': f'Category {category_name} not found.'}), 404)
        return response

    

# User signup route
@app.route('/user/signup', methods=['GET', 'POST'])
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
@app.route('/user/login', methods=['POST'])
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


# Route to purchase property
@app.route('/property/purchase', methods=['POST'])
def purchase_property():
    # Get the user ID, property title, and quantity from the request
    user_id = request.form.get('user_id')
    title = request.form.get('title')
    quantity = int(request.form.get('quantity', 0))

    if not user_id or not title or not quantity:
        return jsonify({'error': 'User ID, property title, and quantity are required.'}), 400

    # Retrieve the user from the database
    user = User.query.get(user_id)
    if not user:
        return jsonify({'error': 'User not found.'}), 404

    # Retrieve the property from the database
    property = Property.query.filter_by(title=title).first()
    if not property:
        return jsonify({'error': 'Property not found.'}), 404

    if property.quantity < quantity:
        return jsonify({'error': 'Insufficient quantity.'}), 400

    # Calculate the total cost
    total_cost = property.price * quantity

    # Create a new bought property entry
    bought_property = BoughtProperty(property=property, user=user, bought_quantity=quantity, total_cost=total_cost)
    db.session.add(bought_property)

    # Update the property quantity
    property.quantity -= quantity

    # Commit the changes to the database
    db.session.commit()

    return jsonify({'message': 'Property purchased successfully.'}), 200


# Route to update the quantity of a bought property
@app.route('/bought/quantity', methods=['PATCH'])
def update_quantity():
    # Get the user ID, property title, and new quantity from the request
    user_id = int(request.form.get('user_id'))
    property_title = request.form.get('property_title')
    new_quantity = int(request.form.get('new_quantity', 0))

    if not user_id or not property_title or not new_quantity:
        return jsonify({'error': 'User ID, property title, and new quantity are required.'}), 400

    # Retrieve the user from the database
    user = User.query.get(user_id)
    if not user:
        return jsonify({'error': 'User not found.'}), 404

    # Retrieve the property from the database
    property = Property.query.filter_by(title=property_title).first()
    if not property:
        return jsonify({'error': 'Property not found.'}), 404

    # Retrieve the associated bought property for the user
    bought_property = BoughtProperty.query.filter_by(property_id=property.property_id, user_id=user.user_id).first()
    if not bought_property:
        return jsonify({'error': 'Bought property not found.'}), 404

    # if property.is_sold:
    #     return jsonify({'error': 'Property is already sold.'}), 400

    if new_quantity > property.quantity:
        return jsonify({'error': 'Insufficient quantity.'}), 400

    # Calculate the total cost based on the new quantity
    total_cost = property.price * new_quantity

    # Update the bought property's quantity and total cost
    bought_property.bought_quantity = new_quantity
    bought_property.total_cost = total_cost

    # Update the property's quantity
    property.quantity += bought_property.bought_quantity - new_quantity

    # Commit the changes to the database
    db.session.commit()

    return jsonify({'message': 'Quantity updated successfully.'}), 200

# Route to view all properties bought by the user on the current day
@app.route('/bought/view/<int:user_id>', methods=['GET'])
def view_bought_properties(user_id):
    # # Get the user ID from the request
    # user_id = int(request.form.get('user_id'))

    if not user_id:
        return jsonify({'error': 'User ID is required.'}), 400
    
    bought_today = []

    # Retrieve all the bought properties for the user on the current day
    bought_properties = BoughtProperty.query.filter(
        BoughtProperty.user_id == user_id,
        BoughtProperty.purchase_date == date.today()
    ).all()

    for bought_property in bought_properties:
        bought_property_dict = bought_property.to_dict()
        bought_today.append(bought_property_dict)

    response = make_response(jsonify({'bought_properties': bought_today}), 200)
    return response

# Route to delete a bought property by product name on the current day
@app.route('/bought/delete', methods=['DELETE'])
def delete_bought_property():
    # Get the user ID and product name from the request
    user_id = int(request.form.get('user_id'))
    product_name = request.form.get('product_name')

    if not user_id or not product_name:
        return jsonify({'error': 'User ID and product name are required.'}), 400

    # Print the user ID and product name for debugging
    print(f'User ID: {user_id}, Product Name: {product_name}')

    # Retrieve the associated bought property for the user, product name, and current day
    bought_property = BoughtProperty.query.join(Property).filter(
        BoughtProperty.user_id == user_id,
        Property.title == product_name,
        BoughtProperty.purchase_date == datetime.today()
    ).first()

    # Print the generated query for debugging
    print(f'Query: {str(db.session.query(bought_property))}')

    if not bought_property:
        return jsonify({'error': 'Bought property not found.'}), 404

    # Delete the bought property
    db.session.delete(bought_property)
    db.session.commit()

    return jsonify({'message': 'Bought property deleted successfully.'}), 200

if __name__ == '__main__':
    app.run(port=5555)