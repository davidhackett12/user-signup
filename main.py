from flask import Flask, request, redirect, render_template
import cgi
import os

app = Flask(__name__)
app.config['DEBUG'] = True

@app.route("/")
def index():
    return render_template('index.html')

@app.route("/success", methods=['POST'])
def success():
    username = request.form['username']
    if len(username) <= 3:
        return redirect("/")

    return render_template('success.html', username=username)

app.run()