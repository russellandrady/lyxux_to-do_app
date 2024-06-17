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
        cur.execute(f"SELECT id, username, email, password FROM users WHERE email='{email}'")
        user = cur.fetchone()
        if user and check_password_hash(user[3], pwd):  # Check if the user exists and password matches
            session['username'] = user[1]
            session['email'] = user[2]
            session['id']=user[0]

            cur.execute("SELECT id, task, completed FROM todos WHERE user_id = %s", (session['id'],))
            todos = cur.fetchall()
            session['todos'] = todos

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

@app.route('/dashboard/create-todo', methods=['POST'])
def createToDo():
    if request.method == 'POST':
        task = request.form['task']
        cur = mysql.connection.cursor()
        cur.execute("INSERT INTO todos (user_id, task, completed) VALUES (%s, %s, %s)", (session['id'], task, False))
        mysql.connection.commit()
        
        cur.execute("SELECT id, task, completed FROM todos WHERE user_id = %s", (session['id'],))
        todos = cur.fetchall()
        session['todos'] = todos
        cur.close()

        flash("Added", 'success')
        return redirect(url_for('dashboard'))

@app.route('/dashboard/update-status', methods=['POST'])
def updateStatus(id, completed):
    if request.method == 'POST':
        cur = mysql.connection.cursor()
        cur.execute("UPDATE todos SET completed=%s WHERE id=%s",
                    (completed, id))
        
        cur.execute("SELECT id, task, completed FROM todos WHERE user_id = %s", (session['id'],))
        todos = cur.fetchall()
        session['todos'] = todos
        cur.close()

        return redirect(url_for('dashboard'))

@app.route('/dashboard/delete-todo/<int:id>', methods=['POST'])
def deleteToDo(id):
    if request.method == 'POST':
        cur = mysql.connection.cursor()
        cur.execute("DELETE FROM todos WHERE id = %s", (id,))
        mysql.connection.commit()

        cur.execute("SELECT id, task, completed FROM todos WHERE user_id = %s", (session['id'],))
        todos = cur.fetchall()
        session['todos'] = todos
        cur.close()

        flash("Deleted", 'success')
        return redirect(url_for('dashboard'))

@app.route('/signout')
def signout():
    session.clear()
    flash("Successfully signed out", 'success')
    return redirect(url_for('login'))

if  __name__ == '__main__':
    app.run(debug = True)