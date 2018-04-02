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
    username_error = request.args.get(username_error)
    password_error = request.args.get(password_error)
    if username_error or password_error:
        username_error = username_error
        password_error = password_error
    else:
        username_error = ""
        password_error = ""
    return render_template('index.html', username_error=username_error, password_error = password_error)

@app.route("/success", methods=['POST'])
def success():
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
        retype_err0r = ""
    
    if "@" or "." not in email:
        email_error = "this is not a valid email"
    else:
        email_error = ""


    if username_error or password_error or retype_error or email_error:
        return render("/", username_error=username_error, password_error=password_error)
    else:
        return render_template('success.html', username=username)

app.run()