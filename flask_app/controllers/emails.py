from crypt import methods
from flask_app import app
from flask import redirect, request, render_template

@app.route('/', methods="POST")
def index():
  return render_template("index.html")