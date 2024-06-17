from flask import Flask, render_template, request, flash, session, url_for, redirect
from flask_mysqldb import MySQL
from werkzeug.security import generate_password_hash
from werkzeug.security import check_password_hash
import os

#flask initialization
app=Flask(__name__)
app.secret_key = os.getenv('SECRET_KEY')

#mysqlconfiguration
app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD']=''
app.config['MYSQL_DB'] = 'todoappdb'

#mysql initialization
mysql = MySQL(app)

@app.route('/login', methods=['GET','POST'])
def login():
    if request.method == 'POST':
        email = request.form['email']
        pwd = request.form['password']
        cur = mysql.connection.cursor()
        cur.execute(f"SELECT username, email, password FROM users WHERE email='{email}'")
        user = cur.fetchone()
        if user and check_password_hash(user[2], pwd):  # Check if the user exists and password matches
            session['username'] = user[0]
            session['email'] = user[1]
            cur.close()
            return redirect(url_for('dashboard'))
        else:
            flash("Invalid data", 'error')
            print(user[2], pwd)
            return render_template('login.html')
    else:
        return render_template('login.html')
@app.route('/register', methods=['GET', 'POST'])
def register():
    reg=False
    if request.method =='POST':
        username = request.form['username']
        email = request.form['email']
        pwd = request.form['password']
        hashed_pwd = generate_password_hash(pwd)
        cur = mysql.connection.cursor()
        cur.execute("insert into users (username, email, password) VALUES (%s, %s, %s)", (username, email, hashed_pwd))
        mysql.connection.commit()
        cur.close()
        flash("Registered Successfully", 'success')
        reg=True
        return render_template('login.html',reg=reg)
    else:
        return render_template('register.html')
    
@app.route('/dashboard')
def dashboard():
    return render_template('dashboard.html')

if  __name__ == '__main__':
    app.run(debug = True)