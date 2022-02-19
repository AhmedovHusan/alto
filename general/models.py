from enum import unique
from general import app
from general import db


class User(db.Model):
    __tablename__ = 'user_table_name'

    id = db.Column(db.Integer(), primary_key=True)
    username = db.Column(db.String(255), unique=True, nullable=False)
    address = db.Column(db.String(300), unique=True, nullable=False)
    password = db.Column(db.String(255), unique=True, nullable=False)

    def __init__(self, username, password, address):
        self.username = username
        self.password = password
        self.address = address


# user_1 = User(username='Husanboy', address='Izboskan', password='Onajonim1234')
# User.query.all()
# db.session.add(user_1)
# db.session.commit()
