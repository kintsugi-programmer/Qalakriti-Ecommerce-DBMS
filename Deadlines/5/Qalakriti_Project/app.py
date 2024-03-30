from flask import Flask, Blueprint,render_template, redirect, url_for, request, session
import pymysql

app = Flask(__name__)

# Set a secret key for session management
app.secret_key = 'your_secret_key'

db_config = {
    'host': 'localhost',
    'user': 'username',
    'password': 'password',
    'database': 'Qalakriti'
}
# admin_blueprint = Blueprint('admin', __name__, url_prefix='/admin')
# app.register_blueprint(admin_blueprint)
# user_blueprint = Blueprint('user', __name__, url_prefix='/user')
# app.register_blueprint(user_blueprint)

def fetch_users():
    connection = pymysql.connect(**db_config)
    cursor = connection.cursor()
    users = {}
    cursor.execute("SELECT usrEmail, usrPassword FROM `User`")  # Update column names
    for email, password in cursor:
        users[email] = {'password': password}
    cursor.close()
    connection.close()
    return users

def fetch_staff():
    connection = pymysql.connect(**db_config)
    cursor = connection.cursor()
    staff = {}
    cursor.execute("SELECT craftEmail, craftPassword FROM Craftsman")
    for email, password in cursor:
        staff[email] = {'password': password}
    cursor.close()
    connection.close()
    return staff

# Define routes
@app.route('/')
def index():
    # Render the home page directly
    return render_template('user/home.html')

@app.route('/user/home')
def user_home():
    # Render the home page for users
    return render_template('user/home.html')

@app.route('/admin')
def admin_dashboard():
    if 'email' in session :
        return render_template('admin/admin_dashboard.html')
    else:
        return redirect(url_for('admin_login'))

@app.route('/admin/login', methods=['GET', 'POST'])
def admin_login():
    if request.method == 'POST':
        count=0
        email = request.form['email']
        password = request.form['password']
        staff = fetch_staff()
        if email in staff and staff[email]['password'] == password:
            session['email'] = email
            return redirect(url_for('admin_dashboard'))
        elif count<=3:
            count+=1
            return render_template('admin/admin_login.html', error='Invalid email or password')
        else:
            return render_template('admin/admin_login.html', error='Too many attempts.')
    return render_template('admin/admin_login.html')



@app.route('/admin/order_management')
def order_management():
    # Render the order management page
    return render_template('admin/order_management.html')

@app.route('/admin/product_management')
def product_management():
    # Render the product management page
    return render_template('admin/product_management.html')

@app.route('/cart')
def cart():
    # Render the shopping cart page
    return render_template('user/cart.html')

@app.route('/checkout')
def checkout():
    # Render the checkout page
    return render_template('user/checkout.html')

@app.route('/confirmation')
def confirmation():
    # Render the order confirmation page
    return render_template('user/confirmation.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        email = request.form['email']
        password = request.form['password']
        users = fetch_users()

        if email in users and users[email]['password'] == password:
            session['email'] = email
            return redirect(url_for('index'))
        else:
            return render_template('user/login.html', error='Invalid email or password')
    return render_template('user/login.html')

@app.route('/orders')
def orders():
    # Render the order history page
    return render_template('user/orders.html')

@app.route('/product')
def product():
    # Render the product details page
    return render_template('user/product.html')

@app.route('/register')
def register():
    # Render the user registration page
    return render_template('user/register.html')


@app.route('/logout')
def logout():
    session.pop('email', None)
    return redirect(url_for('index'))


# Define other routes...
@app.route('/user/add_to_cart')
def add_to_cart():
    #hi
    return



if __name__ == '__main__':
    app.run(debug=True)

