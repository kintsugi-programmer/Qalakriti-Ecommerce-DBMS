from flask import Flask, render_template, request, redirect, url_for
import mysql.connector

app = Flask(__name__)

cart = []

categories = [
    {"name": "Kintsugi Vase", "url": "kintsugi_vase", "image": "img/Kintsugi_Vase.jpg"},
    {"name": "Lavender Candles", "url": "lavender_candles", "image": "img/Lavender_Scented_Candles.jpg"},
    {"name": "Diamond Necklace", "url": "diamond_necklace", "image": "img/Diamond_Necklace.jpg"},
    {"name": "Craftland Chair", "url": "craftland_chair", "image": "img/Craftland_Chair.jpg"},
    {"name": "Vintage Compass", "url": "vintage_compass", "image": "img/Vintage_Compass.jpg"},
    {"name": "Aranmula Kannadi Mirror", "url": "aranmula_kannadi_mirror", "image": "img/Aranmula_Kannadi_Mirror.jpg"},
    {"name": "Madhubani Painting Decor", "url": "madhubani_painting_decor", "image": "img/Madhubani_Painting_Decor.jpg"},
    {"name": "Rajasthani Jewellery Box", "url": "rajasthani_jewellery_box", "image": "img/Rajasthani_Jewellery_Box.png"}
]

imgRoute = {
    'Kintsugi Vase': 'img/Kintsugi_Vase.jpg',
    'Lavender Candles': 'img/Lavender_Scented_Candles.jpg',
    'Diamond Necklace': 'img/Diamond_Necklace.jpg',
    'Craftland Chair': 'img/Craftland_Chair.jpg',
    'Vintage Compass': 'img/Vintage_Compass.jpg',
    'Aranmula Kannadi Mirror': 'img/Aranmula_Kannadi_Mirror.jpg',
    'Madhubani Painting Decor': 'img/Madhubani_Painting_Decor.jpg',
    'Rajasthani Jewellery Box': 'img/Rajasthani_Jewellery_Box.png'
}

product_prices = {
    "Kintsugi Vase": 599.99,
    "Lavender Candles": 799.99,
    "Diamond Necklace": 9999.99,
    "Craftland Chair": 2499.99,
    "Vintage Compass": 1999.99,
    "Aranmula Kannadi Mirror": 3999.99,
    "Madhubani Painting Decor": 1499.99,
    "Rajasthani Jewellery Box": 2999.99
}

db_config = {
    'host': 'localhost',
    'user': 'username',
    'password': 'password',
    'database': 'Qalakriti'
}

def connect_to_database():
    try:
        conn = mysql.connector.connect(**db_config)
        print("Database connected successfully")
        return conn
    except mysql.connector.Error as err:
        print("Error connecting to database:", err)
        return None

def check_user_exists(usrName):
    conn = connect_to_database()
    cursor = conn.cursor()
    sql = "SELECT * FROM login WHERE usrName = %s"
    cursor.execute(sql, (usrName,))
    usrName = cursor.fetchone()
    cursor.close()
    conn.close()
    return usrName

@app.route('/')
def index():
    return render_template('coverpage.html')

@app.route('/register', methods=['GET'])
def registration_form():
    return render_template("register.html")

@app.route('/register', methods=['POST'])
def register():
    usrName = request.form['usrName']
    usrEmail = request.form['usrEmail']
    usrPassword = request.form['usrPassword']
    usrMobNumber = request.form['usrMobNumber']
    usrRegDate = request.form['usrRegDate']

    if check_user_exists(usrName):
        return render_template("register.html", error='User Name already exists. Please choose another User Name.')

    conn = connect_to_database()
    cursor = conn.cursor()
    print("working")

    sql = "INSERT INTO User(usrName, usrEmail, usrPassword, usrMobNumber, usrRegDate) VALUES(%s, %s, %s, %s, %s)"
    val = (usrName, usrEmail, usrPassword, usrMobNumber, usrRegDate)
    cursor.execute(sql, val)
    conn.commit()

    sql = "INSERT INTO login (usrName, usrPassword) VALUES (%s, %s)"
    val = (usrName, usrPassword)
    cursor.execute(sql, val)
    conn.commit()

    cursor.close()
    conn.close()

    return render_template("register.html", error='Registration Successful. Please login to continue.')

@app.route('/login', methods=['GET'])
def login_form():
    return render_template('login.html')

@app.route('/login', methods=['POST', 'PUT'])
def login():
    usrName = request.form['usrName']
    password = request.form['password']
    print("works")
    user = check_user_exists(usrName)
    if(user == None):
        return render_template('login.html', error='Not a registered user. Please register first.')
    print(user)
    if(password != user[1]):
        conn = connect_to_database()
        cur = conn.cursor()
        cur.execute("UPDATE login SET login_attempt = login_attempt + 1 WHERE usrName = %s", (usrName,))
        conn.commit()
        print(user)
        if(user[3] == 'blocked'):
            return redirect(url_for('blocked', usrName=usrName))
        else:
            return render_template('login.html', error='Not a registered user. Please register first.')
    if user and user[1] == password and user[3] == 'allowed':
        conn = connect_to_database()
        cur = conn.cursor()
        cur.execute("UPDATE login SET login_attempt = 0 WHERE usrName = %s", (usrName,))
        conn.commit()
        return redirect(url_for('prod'))
    else:
        return render_template('login.html', error='Not a registered user. Please register first.')

@app.route('/blocked/<usrName>', methods=['GET', 'PUT'])
def blocked(usrName):
    if(request.method == 'PUT'):
        print("put is working")
        conn = connect_to_database()
        cur = conn.cursor()
        cur.execute("UPDATE login SET status = %s WHERE usrName = %s", ('allowed', usrName,))
        n_string = "select * from login where usrName = %s"
        cur.execute(n_string, (usrName,))
        print(cur.fetchone())
        conn.commit()
    return render_template('blocked.html', usrName=usrName)

def enforce_password_policy(password):
    if len(password) < 8:
        return False, "Password must be at least 8 characters long"
    return True, "Password meets the policy requirements"

@app.route('/update_password', methods=['POST'])
def update_password():
    data = request.json
    password = data.get('password')

    is_valid, message = enforce_password_policy(password)

    if is_valid:
        return {'success': True, 'message': 'Password updated successfully'}
    else:
        return {'success': False, 'error': message}

@app.route('/prod', methods=['GET'])
def prod():
    return render_template('/prod.html', categories=categories)

getPrice = "select price from Product where prodType = %s"


@app.route('/prod/<product_url>', methods=['GET', 'POST'])
def product_page(product_url):
    product = next((p for p in categories if p['url'] == product_url), None)
    if not product:
        return "Product not found", 404
    return render_template('product.html', product=product)


@app.route('/cart', methods=['POST'])
def add_to_cart():
    if request.method == 'POST':
        product_url = request.form['product_url']
        product_name = next((p['name'] for p in categories if p['url'] == product_url), None)
        if not product_name:
            return "Product not found", 404

        quantity = int(request.form['quantity'])
        price = product_prices.get(product_name, 0)
        
        # Construct item dictionary
        item = {
            'name': product_name,
            'price': price,
            'quantity': quantity
        }
        cart.append(item)
        print(item)
    return redirect(url_for('view_cart', product_url=product_url))

@app.route('/cart', methods=['GET', 'PUT'])
def view_cart(cart=cart):
    if(request.method == 'PUT'):
        print("put is working")
        cart_body = request.get_json()
        query = "UPDATE product SET stock = stock-1"
        conn = connect_to_database()
        cursor = conn.cursor()
        for item in cart_body:
            print("in the loop")
            cursor.execute(query, (item['quantity'], item['name']))
            print("query executed")
        conn.commit()
        cart.clear()
        return redirect(url_for('prod'))
    return render_template('cart.html', cart=cart, imgRoute=imgRoute)

@app.route('/checkout', methods=['GET', 'POST'])
def checkout():
    if request.method == 'POST':
        # Get the user's order details from the form
        full_name = request.form['full_name']
        address = request.form['address']
        city = request.form['city']
        state = request.form['state']
        zip_code = request.form['zip_code']
        payment_method = request.form['payment_method']
        
        # Process the order and update the database
        conn = connect_to_database()
        cursor = conn.cursor()
        
        # Insert order details into the Order table (assuming an Order table exists)
        order_query = """
        INSERT INTO Orders (full_name, address, city, state, zip_code, payment_method)
        VALUES (%s, %s, %s, %s, %s, %s)
        """
        cursor.execute(order_query, (full_name, address, city, state, zip_code, payment_method))
        order_id = cursor.lastrowid  # Get the ID of the newly created order
        
        # Insert each cart item into the OrderItems table (assuming an OrderItems table exists)
        for item in cart:
            item_query = """
            INSERT INTO OrderItems (order_id, product_name, price, quantity)
            VALUES (%s, %s, %s, %s)
            """
            cursor.execute(item_query, (order_id, item['name'], item['price'], item['quantity']))
        
        # Commit the transaction
        conn.commit()
        
        # Clear the cart
        cart.clear()
        
        cursor.close()
        conn.close()
        
        return redirect(url_for('order_confirmation', order_id=order_id))
    
    return render_template('checkout.html', cart=cart)

@app.route('/order_confirmation/<int:order_id>', methods=['GET'])
def order_confirmation(order_id):
    return render_template('order_confirmation.html', order_id=order_id)

if __name__ == '__main__':
    app.run(debug=True, port=5000)
