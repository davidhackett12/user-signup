from flask import Flask, request, redirect, render_template
import cgi
import os

app = Flask(__name__)
app.config['DEBUG'] = True


@app.route("/")
def index():
    username_error = ""
    password_error = ""
    retype_error = ""
    email_error = ""
    return render_template('index.html', username_error=username_error, password_error = password_error, retype_error=retype_error)

@app.route("/", methods=['POST'])
def validate():
    username = request.form['username']
    password = request.form['password']
    retype_password = request.form['retype_password']
    email = request.form['email']
    if len(username) <= 2 or len(username) >= 21:
        username_error = "username is not the right length"
    elif " " in username:
        username_error = "username cannot include spaces"
    elif username == "":
        usernname_error = "no username is entered" 
    else:
        username_error = ""

    if password == "":
        password_error = "you did not enter a password"
    elif len(password) <= 2 or len(password) >= 21:
        password_error = "password is not the right length"
    else:
        password_error = ""
    
    if retype_password != password:
        retype_error = "passwords do not match"
    else:
        retype_error = ""
    
    if email == "":
        email_error = ""
    elif email.count('@') != 1 or email.count('.') != 1:
        email_error = "this is not a valid email"
    elif len(email) > 20 or len(email) < 3:
        email_error = "this is not a valid email"
    elif " " in email:
        email_error = "this is not a valid email"
    else:
        email_error = ""
    
    if username_error or password_error or retype_error or email_error:
        return render_template('index.html', username_error=username_error, password_error = password_error, retype_error=retype_error)
    else:
        return redirect("/success?username="+username)

@app.route("/success")
def success():
    username = request.args.get('username')
    return render_template('success.html', username=username)

app.run()