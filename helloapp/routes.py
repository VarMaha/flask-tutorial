from flask import render_template
from helloapp import app
@app.route("/")
@app.route("/home")
def home():
   return render_template("index.html",title="Title Page of Hello App")

users=["John","David","Travis","George","Victor"]

@app.route("/user/<username>")
def hello_user(username):
    return render_template("user.html",title="Users Page",user=username)

@app.route("/users")
def list_users():
    return render_template("index.html",title="Users Page",users=users)

@app.route("/about")
def about():
   return "<h1>About page</h1>"

