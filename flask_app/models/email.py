EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')
from unittest import result
from winreg import QueryInfoKey
from wsgiref import validate
from flask import flash
import re
from flask_app import app
from flask_app.config.mysqlconnection import connectToMySQL

class Email:
  db = "email_validation"
  def __init__(self,data):
    self.id = data['id']
    self.email = data['email']
    self.updated_at = data['updated_at']
    self.created_at = data['created_at']

  @classmethod
  def create(cls,data):
    query = "INSERT INTO email_validation(name, created_at) VALUES (%(email)s, NOW())"
    result = connectToMySQL(cls.db).query_db(query,data)
    return result

  @classmethod
  def show(cls):
    query = "SELECT * FROM email_validation"
    result = connectToMySQL(cls.db).query_db(query)
    print(result)
    email = []
    for e in result:
      email.append(cls(e))
    return email
  
  @classmethod
  def delete(cls,data):
    query = "DELETE FROM email_validation WHERE id = %(id)s;"
    return connectToMySQL(cls.db).query_db(query, data)
  
  @staticmethod
  def validate(email):
    validate = True
    query = "SELECT * FROM email_validation WHERE email = %(email)s"
    results = connectToMySQL(Email.db).query_db(query,email)
    if len(results) >= 1:
      flash("Email is already taken!")
      validate = False
    if not EMAIL_REGEX.match(email['email']):
      flash('Invalid Email')
      validate = False
    return validate
    
    # validate = True
    # if not EMAIL_REGEX.match(email['email']):
    #   flash("EMAIL NOT VALID!!!")
    #   validate = False
    # return validate
  