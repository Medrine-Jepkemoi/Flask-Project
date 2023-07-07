from flask import Flask, request, make_response, jsonify, json, session
from datetime import date
from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS


from models import db, User, Admin, Property, PropertyCategory, BoughtProperty
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///app.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['JSONIFY_PRETTYPRINT_REGULAR'] = True
app.secret_key = b'\xf6\xdc\\\xd8P\x98\xe8\x0c\xbal\x8c\x8c\x7f7K\xc8'

CORS(app)

migrate = Migrate(app, db)

db.init_app(app)



# Index route
@app.route('/')
def index():
    return "Index for Nyumba Mali"

# User CRUD
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
        new_acc.set_password(password)

        db.session.add(new_acc)
        db.session.commit()

        user_dict = new_acc.to_dict()

        response = make_response(
            jsonify(user_dict),
            201
        )

    response.headers['Access-Control-Allow-Origin'] = '*'  # Allow cross-origin requests
    session['user_id'] = new_acc.user_id  # Create a session and store the user ID
    return response

# User login route
@app.route('/user/login', methods=['POST'])
def login():
    data = request.get_json()
    email = data.get('email')
    password = data.get('password')

    if not email or not password:
        response = make_response(jsonify({'error': 'Email and password are required.'}), 400)
        return response

    user = User.query.filter_by(email=email).first()

    if not user:
        response = make_response(jsonify({'error': 'Invalid email or password.'}), 401)
        return response

    if not user.check_password(password):
        response = make_response(jsonify({'error': 'Invalid email or password.'}), 401)
        return response
    # if user.password != password:
    #     response = make_response(jsonify({'error': 'Invalid email or password.'}), 401)
    #     return response

    # User login successful
    response = make_response(jsonify({'message': 'Login successful.'}), 200)
    session['user_id'] = user.user_id  # Create a session and store the user ID
    return response

# User login route
# @app.route('/user/login', methods=['POST'])
# def login():
#     email = request.form.get("email")
#     password = request.form.get("password")

#     if not email or not password:
#         response = make_response(jsonify({'error': 'Email and password are required.'}), 400)
#         return response

#     user = User.query.filter_by(email=email).first()

#     if not user:
#         response = make_response(jsonify({'error': 'Invalid email or password.'}), 401)
#         return response

#     if user.password != password:
#         response = make_response(jsonify({'error': 'Invalid email or password.'}), 401)
#         return response

#     # User login successful
#     response = make_response(jsonify({'message': 'Login successful.'}), 200)
#     session['user_id'] = user.user_id  # Create a session and store the user ID
#     return response




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

# Route to purchase property
@app.route('/property/purchase', methods=['POST'])
def purchase_property():
    user_id = session.get('user_id')  # Retrieve the user ID from the session
    title = request.form.get('title')
    quantity = int(request.form.get('quantity', 0))

    if not user_id or not title or not quantity:
        return jsonify({'error': 'User ID, property title, and quantity are required.'}), 400

    user = User.query.get(user_id)
    if not user:
        return jsonify({'error': 'User not found.'}), 404

    property = Property.query.filter_by(title=title).first()
    if not property:
        return jsonify({'error': 'Property not found.'}), 404

    if property.quantity < quantity:
        return jsonify({'error': 'Insufficient quantity.'}), 400

    total_cost = property.price * quantity

    bought_property = BoughtProperty(property=property, user=user, bought_quantity=quantity, total_cost=total_cost)
    db.session.add(bought_property)

    property.quantity -= quantity

    db.session.commit()

    return jsonify({'message': 'Property purchased successfully.'}), 200


# View cart
@app.route('/user/cart', methods=['GET'])
def view_cart():
    user_id = session.get('user_id')  # Retrieve the user ID from the session

    if not user_id:
        return jsonify({'error': 'User not logged in.'}), 401

    user = User.query.get(user_id)
    if not user:
        return jsonify({'error': 'User not found.'}), 404

    cart = BoughtProperty.query.filter_by(user_id=user_id).all()
    cart_items = []

    for item in cart:
        property_data = {
            'property_id': item.property.property_id,
            'title': item.property.title,
            'image': item.property.image,
            'description': item.property.description,
            'price': item.property.price,
            'quantity': item.bought_quantity,
            'total_cost': item.total_cost,
        }
        cart_items.append(property_data)

    response = make_response(jsonify({'cart': cart_items}), 200)
    return response


# Route to update the quantity of a bought property
@app.route('/bought/quantity', methods=['PATCH'])
def update_quantity():
    user_id = session.get('user_id')  # Retrieve the user ID from the session
    property_title = request.form.get('property_title')
    new_quantity = int(request.form.get('new_quantity', 0))

    if not user_id or not property_title or not new_quantity:
        return jsonify({'error': 'User ID, property title, and new quantity are required.'}), 400

    user = User.query.get(user_id)
    if not user:
        return jsonify({'error': 'User not found.'}), 404

    property = Property.query.filter_by(title=property_title).first()
    if not property:
        return jsonify({'error': 'Property not found.'}), 404

    bought_property = BoughtProperty.query.filter_by(property_id=property.property_id, user_id=user.user_id).first()
    if not bought_property:
        return jsonify({'error': 'Bought property not found.'}), 404

    if new_quantity > property.quantity:
        return jsonify({'error': 'Insufficient quantity.'}), 400

    total_cost = property.price * new_quantity

    bought_property.bought_quantity = new_quantity
    bought_property.total_cost = total_cost

    property.quantity += bought_property.bought_quantity - new_quantity

    db.session.commit()

    return jsonify({'message': 'Quantity updated successfully.'}), 200


# Route to delete a property from the cart
@app.route('/user/cart/<int:property_id>', methods=['DELETE'])
def delete_from_cart(property_id):
    user_id = session.get('user_id')  # Retrieve the user ID from the session

    if not user_id:
        return jsonify({'error': 'User not logged in.'}), 401

    user = User.query.get(user_id)
    if not user:
        return jsonify({'error': 'User not found.'}), 404

    bought_property = BoughtProperty.query.filter_by(property_id=property_id, user_id=user_id).first()
    if not bought_property:
        return jsonify({'error': 'Property not found in the cart.'}), 404

    property = Property.query.get(property_id)
    if not property:
        return jsonify({'error': 'Property not found.'}), 404

    property.quantity += bought_property.bought_quantity

    db.session.delete(bought_property)
    db.session.commit()

    return jsonify({'message': 'Property removed from the cart.'}), 200

# User logout route
@app.route('/user/logout', methods=['POST'])
def user_logout():
    # Clear the user session
    session.clear()

    response = make_response(jsonify({'message': 'Logout successful.'}), 200)
    return response



# ADMIN CRUD
# Sign up route for admin
@app.route('/admin/signup', methods=['POST'])
def admin_signup():
    # Check if an admin already exists
    existing_admin = Admin.query.first()
    if existing_admin:
        response = make_response(jsonify({'error': 'Admin already exists.'}), 409)
        return response

    email = request.form.get('email')
    password = request.form.get('password')

    # Create a new admin
    admin = Admin(email=email, password=password)
    admin.set_password(password)
    db.session.add(admin)
    db.session.commit()

    response = make_response(jsonify({'message': 'Admin signup successful.'}), 201)
    return response

@app.route('/admin/<int:admin_id>', methods=['DELETE'])
def delete_admin(admin_id):
    admin = Admin.query.get(admin_id)

    if not admin:
        return jsonify({'error': 'Admin not found'}), 404

    db.session.delete(admin)
    db.session.commit()

    return jsonify({'message': 'Admin deleted successfully'})

# Login route for admin
@app.route('/admin/login', methods=['POST'])
def admin_login():
    email = request.form.get('email')
    password = request.form.get('password')

    # Find the admin by email
    admin = Admin.query.filter_by(email=email).first()

    if not admin or admin.password != password:
        response = make_response(jsonify({'error': 'Invalid email or password.'}), 401)
        return response

    response = make_response(jsonify({'message': 'Admin login successful.'}), 200)
    return response


@app.route('/admin/products', methods=['GET'])
def get_products():
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
            'category_id': category.category_id,
            'category_name': category_name, 
        }
        products_list.append(product_data)

    response = make_response(jsonify(products_list), 200)   
    return response

# View property categories route
@app.route('/admin/property/categories', methods=['GET'])
def view_property_categories():
    categories = PropertyCategory.query.all()

    categories_list = []
    for category in categories:
        category_data = {
            'category_id': category.category_id,
            'category_name': category.category_name,
        }
        categories_list.append(category_data)

    response = make_response(jsonify(categories_list), 200)
    return response

# Create property route
@app.route('/admin/property', methods=['POST'])
def create_property():
    title = request.form.get('title')
    description = request.form.get('description')
    price = int(request.form.get('price'))
    category_id = int((request.form.get('category_id')))
    image = (request.form.get('image'))
    quantity = int((request.form.get('quantity')))
    admin_id = int((request.form.get('admin_id')))


    property = Property(title=title, description=description, price=price, category_id=category_id, image=image, quantity=quantity, admin_id=admin_id)
    db.session.add(property)
    db.session.commit()

    response = make_response(jsonify({'message': 'Property created successfully.'}), 201)
    return response

# Route to create a product category
@app.route('/admin/category', methods=['POST'])
def create_category():
    category_name = request.form.get('category_name')

    if not category_name:
        return jsonify({'error': 'Category name is required.'}), 400

    # Check if the category already exists
    existing_category = PropertyCategory.query.filter_by(category_name=category_name).first()
    if existing_category:
        return jsonify({'error': 'Category already exists.'}), 400

    # Create a new category
    new_category = PropertyCategory(category_name=category_name)
    db.session.add(new_category)
    db.session.commit()

    return jsonify({'message': 'Category created successfully.'}), 201


# Update property route
@app.route('/admin/property/<int:property_id>', methods=['PATCH'])
def update_property(property_id):
    property = Property.query.get(property_id)

    if not property:
        response = make_response(jsonify({'error': 'Property not found.'}), 404)
        return response

    new_price = request.form.get('price')
    new_quantity = request.form.get('quantity')

    if new_price:
        property.price = int(new_price)
    
    if new_quantity:
        property.quantity = int(new_quantity)

    db.session.commit()

    response = make_response(jsonify({'message': 'Property updated successfully.'}), 200)
    return response

# Delete property route
@app.route('/admin/property/<int:property_id>', methods=['DELETE'])
def delete_property(property_id):
    property = Property.query.get(property_id)

    if not property:
        response = make_response(jsonify({'error': 'Property not found.'}), 404)
        return response

    db.session.delete(property)
    db.session.commit()

    response = make_response(jsonify({'message': 'Property deleted successfully.'}), 200)
    return response
if __name__ == '__main__':
    app.run(port=5555)
