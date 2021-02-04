from dealership_api import app, db, login_manager
import uuid
from datetime import datetime

#Adding Flask Security for Passwords
from werkzeug.security import generate_password_hash, check_password_hash

# import for secrets module (given by python)
import secrets

# Imports for login manager
from flask_login import UserMixin


@login_manager.user_loader
def load_user(user_id):
    return User.query.get(user_id)
	#query methods finds values in user_id. 
	#similar to SELECT "user"_id in SQL

class User(db.Model, UserMixin):
    id = db.Column(db.String, primary_key = True)
    first_name = db.Column(db.String(150), nullable = True, default = '')
    last_name = db.Column(db.String(150), nullable = True, default = '')
    email = db.Column(db.String(150), nullable = False)
    password = db.Column(db.String, nullable = True, default = '')
    g_auth_verify = db.Column(db.Boolean, default = False)
    token = db.Column(db.String, default = '')
    date_created = db.Column(db.DateTime, nullable = False, default = datetime.utcnow)

    def __init__(self,email,first_name = '', last_name = '', id = '', password = '', g_auth_verify = False):
        self.id = self.set_id()
        self.first_name = first_name
        self.last_name = last_name
        self.password = self.set_password(password)
        self.email = email
        self.token = self.set_token(24)
        self.g_auth_verify = g_auth_verify

    def set_token(self, length):
        return secrets.token_hex(length)

    def set_id(self):
        return str(uuid.uuid4())

    def set_password(self, password):
        self.pw_hash = generate_password_hash(password)
        return self.pw_hash
    
    def __repr__(self):
        return f'User {self.email} has been added to the database'