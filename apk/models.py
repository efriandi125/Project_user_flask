from datetime import datetime
from app import db
class Users(db.Model):
    id=db.Column(db.Integer,primary_key=True)
    email=db.Column(db.String(50),nullable=False)
    first_name=db.Column(db.String(50),nullable=False)
    last_name=db.Column(db.String(50),nullable=False)
    avatar=db.Column(db.String(100),nullable=False)
    created_at=db.Column(db.DATETIME)
    updated_at=db.Column(db.DATETIME)
    deleted_at=db.Column(db.DATETIME)