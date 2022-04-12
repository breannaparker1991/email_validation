from flask_app import app
from flask import redirect, request, render_template
from flask_app.models.email import Email

@app.route('/')
def index():
  return render_template("index.html")

@app.route('/new', methods=["POST"])
def new():
  if not Email.validate(request.form):
    return redirect('/')
  Email.create(request.form)
  return redirect('/show')

  # data = {
  #   "email": request.form['email']
  # }
  # Email.create(data)

@app.route('/show')
def show():
  return render_template("show.html", emails = Email.show())

@app.route('/delete/<int:id>')
def delete(id):
  data = {
    "id" : id
  }
  Email.delete(data)
  return redirect('/show')