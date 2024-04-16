from flask import Flask, render_template, redirect, url_for, request, session
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

@app.route('/')
def index():
    # Render the home page directly
    return render_template('user/home.html')

@app.route('/admin')
def admin_dashboard():
    if 'email' in session:
        return render_template('admin/admin_dashboard.html')
    else:
        return redirect(url_for('admin_login'))

@app.route('/admin/login', methods=['GET', 'POST'])
def admin_login():
    if request.method == 'POST':
        email = request.form['email']
        password = request.form['password']
        staff = fetch_staff()
        if email in staff and staff[email]['password'] == password:
            session['email'] = email
            return redirect(url_for('admin_dashboard'))
        else:
            return render_template('admin/admin_login.html', error='Invalid email or password')
    return render_template('admin/admin_login.html')


