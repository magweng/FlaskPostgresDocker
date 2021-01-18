from project import db
from datetime import datetime as dt


# class User(db.Model):
#     __tablename__ = "users"

#     id = db.Column(db.Integer, primary_key=True)
#     email = db.Column(db.String(128), unique=True, nullable=False)
#     active = db.Column(db.Boolean(), default=True, nullable=False)

#     def __init__(self, email):
#         self.email = email


class LogMessage(db.Model):
    __tablename__ = "log_message"

    id = db.Column(db.Integer, primary_key=True)
    datetime = db.Column(db.DateTime, default=dt.now(), nullable=False)
    message = db.Column(db.Text, nullable=True)

    def __init__(self, datetime, message):
        self.datetime = datetime
        self.message = message

    def __repr__(self):
        return '<Log_message {}>'.format(self.message)
