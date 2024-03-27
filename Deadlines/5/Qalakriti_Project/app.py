from flask import Flask, render_template, request, redirect, url_for
import pymysql

app = Flask(__name__)

# Database connection
connection = pymysql.connect(host='localhost',
                             user='username',
                             password='password',
                             database='Qalakriti',
                             cursorclass=pymysql.cursors.DictCursor)

# Define routes
@app.route('/')
def index():
    return render_template('index.html')

@app.route('/admin')
def admin_dashboard():
    return render_template('admin/admin_dashboard.html')

@app.route('/admin/login')
def admin_login():
    return render_template('admin/admin_login.html')

@app.route('/admin/order_management')
def order_management():
    return render_template('admin/order_management.html')

@app.route('/admin/product_management')
def product_management():
    return render_template('admin/product_management.html')

@app.route('/user/cart')
def cart():
    return render_template('user/cart.html')

@app.route('/user/checkout')
def checkout():
    return render_template('user/checkout.html')

@app.route('/user/confirmation')
def confirmation():
    return render_template('user/confirmation.html')

@app.route('/user/home')
def home():
    return render_template('user/home.html')

@app.route('/user/login')
def login():
    return render_template('user/login.html')

@app.route('/user/orders')
def orders():
    return render_template('user/orders.html')

@app.route('/user/product')
def product():
    return render_template('user/product.html')

@app.route('/user/register')
def register():
    return render_template('user/register.html')

if __name__ == '__main__':
    app.run(debug=True)
