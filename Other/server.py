from flask import Flask, render_template, request, redirect, url_for, send_from_directory
import mysql.connector
import os
app = Flask(__name__)

# MySQL database configuration
db_config = {
    'host': 'localhost',
    'user': 'root',
    'password': 'root',
    'database': 'hel'
}

# Function to connect to MySQL database
def connect_to_database():
    try:
        conn = mysql.connector.connect(**db_config)
        print("Database connected successfully")
        return conn
    except mysql.connector.Error as err:
        print("Error connecting to database:", err)
        return None

# Function to check if a user exists in the database
def check_user_exists(username):
    conn = connect_to_database()
    cursor = conn.cursor()
    sql = "SELECT * FROM Register WHERE username = %s"
    cursor.execute(sql, (username,))
    user = cursor.fetchone()
    cursor.close()  
    conn.close()
    return user

# Route for the registration form
@app.route('/', methods=['GET'])
def registration_form():
    return render_template("register.html")

# Route to handle form submission for registration
@app.route('/', methods=['POST'])
def register():
    name = request.form['name']
    username = request.form['username']
    password = request.form['password']
    contact = request.form['contact']
    if check_user_exists(username):
        return "Username already exists. Please choose another username."

    # Connect to the database
    conn = connect_to_database()
    cursor = conn.cursor()
    print("working")
    # Insert user data into the database
    sql = "INSERT INTO register (name, username, password, contact_number) VALUES (%s, %s, %s, %s)"
    val = (name, username, password, contact)
    cursor.execute(sql, val)
    conn.commit()

    # Insert user data into the database
    sql = "INSERT INTO login (username, password) VALUES (%s, %s)"
    val = (username, password)
    cursor.execute(sql, val)
    conn.commit()


    # Close database connection
    cursor.close()
    conn.close()

    return redirect(url_for('registration_success'))

# Route to show registration success message
@app.route('/success')
def registration_success():
    return render_template('success.html')

# Route for login page
@app.route('/login',  methods=['GET'])
def login_form():
    return render_template('login.html')

# Route to handle form submission for login
@app.route('/login', methods=['POST'])
def login():
    print("works")
    username = request.form['username']
    password = request.form['password']
    print("works")
    # Check if the user exists in the database
    user = check_user_exists(username)
    print(user)
    if user and user[2] == password:
        return redirect(url_for('website'))
    else:
        return redirect(url_for('registration_form'))  # Redirect to registration page if user not registered

# Route to show login success message
@app.route('/login_success')
def login_success():
    return render_template('login_success.html')

@app.route('/website',methods=['GET'])
def website():
    return render_template('website.html')


@app.route('/phone',methods=['GET', 'POST'])
def phones():
    return render_template('phone.html')

@app.route('/headphone',methods=['GET', 'POST'])
def headphones():
    return render_template('headphone.html')

@app.route('/robots',methods=['GET', 'POST'])
def robots():
    return render_template('robots.html')

@app.route('/fridge',methods=['GET', 'POST'])
def fridge():
    return render_template('fridge.html')

@app.route('/loudspeaker',methods=['GET', 'POST'])
def speaker():
    return render_template('loudspeaker.html')

@app.route('/television',methods=['GET', 'POST'])
def televison():
    return render_template('television.html')

@app.route('/air_conditioner',methods=['GET', 'POST'])
def ac():
    return render_template('ac.html')

@app.route('/laptop',methods=['GET', 'POST'])
def laptop():
    return render_template('laptop.html')


def count_login_attempts(count):
    if count<3:
        count+=1
    elif count==3:
        print("You have exceeded the limit of login attempts")
        return render_template('block.html')

if __name__ == '__main__':
    app.run(debug=True,port=3000)