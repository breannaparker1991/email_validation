from flask_app.config.mysqlconnection import connectToMySQL

class Email:
  db = "email_validation"
  def __init__(self,data):
    self.id = data['id']
    self.email = data['email']
    self.updated_at = data['updated_at']
    self.created_at = data['created_at']

