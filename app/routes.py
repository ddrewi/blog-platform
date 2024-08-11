from flask import render_template
from app import app

@app.route("/")
@app.route("/index")
def index():
    user = {"username": "Andrew"}
    posts = [
        {
            "author": {"username": "John"},
            "body": "Just woke up!"
        },
        {
            "author": {"username": "Amy"},
            "body": "Ate some delicious food :)"
        }
    ]
    return render_template("index.html", title="Home", user=user, posts=posts)
