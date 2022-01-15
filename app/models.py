from datetime import datetime
from app import db
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import UserMixin
from app import login

class User(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(64), index=True, unique=True)
    email = db.Column(db.String(120), index=True, unique=True)
    password_hash = db.Column(db.String(128))

    def __repr__(self):
        return '<User {}>'.format(self.username)
    def set_password(self, password):
        self.password_hash = generate_password_hash(password)
    def check_password(self, password):
        return check_password_hash(self.password_hash, password)

class Post(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    body = db.Column(db.String(140))
    timestamp = db.Column(db.DateTime, index=True, default=datetime.utcnow)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))

    def __repr__(self):
        return '<Post {}>'.format(self.body)


@login.user_loader
def load_user(id):
    
    return User.query.get(int(id))

class Product(db.Model):
    
    id = db.Column (db.Integer, primary_key=True)
    product_name = db.Column (db.String(64))
    product_link = db.Column (db.String(120), unique=True)
    user_id = db.Column (db.Integer, db.ForeignKey('user.id'))

    def __repr__(self):
        return '<Product {}>'.format(self.product_name)

class Price(db.Model):

    actual_price = db.Column (db.Integer, primary_key = True)
    product_id = db.Column (db.Integer, db.ForeignKey('product.id'))
    change_date = db.Column (db.DateTime)
    change_price = db.Column (db.String(64))

    def __repr__(self):
        return '<Price {} {} {}>'.format(self.product_id, self.change_date, self.change_price)