from flask import (
    Flask, request, url_for,
    render_template
    )
from markupsafe import escape
from werkzeug.utils import secure_filename

app = Flask(__name__)

@app.route("/notSafe")
def hello():
    script = request.args.get("script", "XSS atack")
    return f"<h1>Hello World<h2>\n{script}" # Breach for XSS atacks


@app.route("/safe")
def helloSafe():
    script = request.args.get("script", "safe")
    return f"{escape(script)}" # escape method prevents XSS atacks

@app.post("/login")
def login():
    username = request.form['username']
    return render_template('uploadFile.html', username=escape(username))

@app.post("/upload")
def upload():
    file = request.files['userFile']
    username = request.form['username']
    file.save(f'var/www/uploads/{secure_filename(file.filename)}')
    return render_template('userLogged.html', username=escape(username))


@app.get("/")
def index():
    return render_template("index.html")

with app.test_request_context("/hello", method = "GET"):
    print(url_for("index"))
    print(url_for("index", username="My Name Here"))
    print(url_for("static", filename="index.css"))
    assert request.path == "/hello"
    assert request.method == "GET"