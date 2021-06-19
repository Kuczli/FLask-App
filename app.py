from flask import Flask,render_template, url_for, redirect
from AzureDB import AzureDB
from datetime import datetime
from flask_dance.contrib.github import make_github_blueprint, github
import secrets
import os

app = Flask(__name__)
app.secret_key = secrets.token_hex(16) #generujemy sekretny klucz aplikacji
os.environ['OAUTHLIB_INSECURE_TRANSPORT'] = '1' #zezwalamy na polaczenie w lokalnym
#srodowisku bez https

github_blueprint = make_github_blueprint(
    client_id="061455c87c668f8d2a92", #tu wklek swoj wygenerowany id z github
    client_secret="868719a58866e5bad814350c8c42875526b7447f",#tu wklej swoj
#wygenerowany client secret z github
)

app.register_blueprint(github_blueprint, url_prefix='/login')
@app.route('/')
def github_login():
    if not github.authorized:
        return redirect(url_for('github.login'))
    else:
        account_info = github.get('/user')
        if account_info.ok:
            account_info_json = account_info.json()
            return render_template("index.html")
        return '<h1>Request failed!</h1>'

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

@app.route('/ksiega-gosci')
def ksiegagosci():
    with AzureDB() as a:
        data = a.azureGetData()
    return render_template("ksiegagosci.html", data = data)



@app.errorhandler(404)
def not_found_error(error):
    return render_template("404.html"), 404

if __name__ == '__main__':
    app.run(debug=True)

