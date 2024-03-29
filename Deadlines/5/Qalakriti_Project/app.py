from flask import Flask, render_template, redirect, url_for

app = Flask(__name__)

# Define routes
@app.route('/')
def index():
    # Render the home page directly
    return render_template('user/home.html')

@app.route('/home')
def home():
    # Render the home page
    return render_template('user/home.html')

@app.route('/admin')
def admin_dashboard():
    # Render the admin dashboard page
    return render_template('admin/admin_dashboard.html')

@app.route('/admin/login')
def admin_login():
    # Render the admin login page
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

@app.route('/login')
def login():
    # Render the user login page
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

if __name__ == '__main__':
    app.run(debug=True)
