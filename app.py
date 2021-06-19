from flask import Flask,render_template, url_for

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

@app.errorhandler(404)
def not_found_error(error):
    return render_template("404.html"), 404

if __name__ == '__main__':
    app.run(debug=True)

