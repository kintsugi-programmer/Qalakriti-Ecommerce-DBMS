from flask import Flask, render_template, request, redirect, url_for
import pymysql

app = Flask(__name__)

# Database connection
connection = pymysql.connect(host='localhost',
                             user='username',
                             password='password',
                             database='Qalakriti',
                             cursorclass=pymysql.cursors.DictCursor)

# Routes
@app.route('/')
def index():
    return render_template('user/home.html')

@app.route('/login')
def login():
    return render_template('user/login.html')

# Other routes...

if __name__ == "__main__":
    app.run(debug=True)
