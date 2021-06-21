from flask import Flask,render_template, url_for, redirect, request
from AzureDB import AzureDB
from datetime import datetime
from flask_dance.contrib.github import make_github_blueprint, github
import secrets
import os

app = Flask(__name__)




@app.route('/')
def home():
    return render_template("index.html")

@app.route('/about_me')
def about_me():
    return render_template("about_me.html")


@app.route('/gallery')
def gallery():
    return render_template("gallery.html")

@app.route('/contact')
def contact():
    return render_template("contact.html")

@app.route('/ksiega_gosci', methods=['POST'])
def ksiega_gosci_form():
    with AzureDB() as a:
        a.azureAddData(request.form.get("nickname"), request.form.get("content"), request.form.get("date"))
    return redirect('ksiega_gosci')


@app.errorhandler(404)
def not_found_error(error):
    return render_template("404.html"), 404

if __name__ == '__main__':
    app.run(debug=True)

