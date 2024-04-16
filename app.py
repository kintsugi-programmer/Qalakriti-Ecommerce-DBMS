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

def fetch_users():
    connection = pymysql.connect(**db_config)
    cursor = connection.cursor()
    users = {}
    cursor.execute("SELECT usrEmail, usrPassword FROM User")  # Update column names
    for email, password ,usrFA in cursor:
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
    return render_template('home.html')

@app.route('/craftsman/login', methods=['GET', 'POST'])
def craftsman_login():
    if request.method == 'POST':
        connection = pymysql.connect(**db_config)
        cursor = connection.cursor()
        email = request.form['email']
        password = request.form['password']
        staff = fetch_staff()
        if email not in staff:
            return render_template('craftsman/cn_login.html', error='Not a registered Craftartist. Please register first.')
        elif email in staff and staff[email]['password'] == password:
            session['email'] = email
            return redirect(url_for('cn_dashboard')) # refer to the python function cn_dashboard
        else:
            return render_template('craftsman/cn_login.html', error='Invalid email or password')
        
    return render_template('craftsman/cn_login.html')

@app.route('/user/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        connection = pymysql.connect(**db_config)
        cursor = connection.cursor()
        email = request.form['email']
        password = request.form['password']
        users = fetch_users()
        
        if email not in users:
            return render_template('user/ur_login.html', error='Not a registered user. Please register first.')
        elif email in users and users[email]['password'] == password:
            session['email'] = email
            return redirect(url_for('ur_dashboard'))
        else:
            return render_template('user/ur_login.html', error='Invalid email or password')
    return render_template('user/ur_login.html')

# route for user register webpage
@app.route('/user/register',methods=['GET','POST'])
def ur_register():
    if request.method == 'POST':
        connection = pymysql.connect(**db_config)
        cursor = connection.cursor()

        usrName = request.form['usrName']
        usrEmail = request.form['usrEmail']
        usrPassword = request.form['usrPassword']
        usrMobNumber = request.form['usrMobNumber']
        usrRegDate = request.form['usrRegDate']

        cursor.execute("INSERT INTO User(usrName, usrEmail, usrPassword, usrMobNumber, usrRegDate) VALUES(%s, %s, %s, %s, %s)", (usrName, usrEmail, usrPassword, usrMobNumber, usrRegDate)) # Update column names
        connection.commit()  # Corrected
        cursor.close()
        connection.close()
        return render_template('user/ur_login.html', error='Registration Successful. Please login to continue.')

    return render_template('user/ur_register.html')

@app.route('/craftsman/register',methods=['GET','POST'])
def cn_register():
    if request.method == 'POST':
        connection = pymysql.connect(**db_config)
        cursor = connection.cursor()

        craftName = request.form['craftName']
        craftEmail = request.form['craftEmail']
        craftPassword = request.form['craftPassword']
        craftMobNumber = request.form['craftMobNumber']
        craftBusType = request.form['craftBusType']

        cursor.execute("INSERT INTO Craftsman(craftName, craftEmail, craftPassword, craftMobNumber, craftBusType) VALUES(%s, %s, %s, %s, %s)", (craftName, craftEmail, craftPassword, craftMobNumber, craftBusType)) # Update column names
        connection.commit()  # Corrected
        cursor.close()
        connection.close()
        return render_template('craftsman/cn_login.html', error='Registration Successful. Please login to continue.')

    return render_template('craftsman/cn_register.html')

@app.route('/craftsman/cn_dashboard')
def cn_dashboard():
    # Your view function logic here
    return render_template('craftsman/cn_dashboard.html')

@app.route('/user/ur_dashboard')
def ur_dashboard():
    # Your view function logic here
    return render_template('user/ur_dashboard.html')


if __name__ == '__main__':
    app.run(debug=True)

