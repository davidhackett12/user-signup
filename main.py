from flask import Flask, request, redirect, render_template
import cgi
import os

app = Flask(__name__)
app.config['DEBUG'] = True


@app.route("/")
def index():
    username_error = ""
    username_error = request.args.get(username_error)
    if username_error:
        username_error = username_error
    else:
        username_error = ""
    return render_template('index.html', username_error=username_error)

@app.route("/success", methods=['POST'])
def success():
    username = request.form['username']
    password = request.form['password']
    if len(username) <= 3 or len(username) >= 20:
        username_error = "username is not the right length"
    elif " " in username:
        username_error = "username cannot include spaces"
    elif username == "":
        usernname_error = "no username is entered" 
    else:
        username_error = ""

    if password == "":
        password_error = "you did not enter a password"
    elif len(password) <= 3 or len(password) >= 20:
        password_error = "password is not the right length"
    else:
        password_error = ""


    if username_error or password_error:
        return redirect("/?=", username_error=username_error, password_error= password_error)
    else:
        return render_template('success.html', username=username)

app.run()