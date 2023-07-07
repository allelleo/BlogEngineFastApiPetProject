from .db import db
from peewee import Model, CharField, IntegerField, DateTimeField, TextField


class Admin(db.Model):
    username = CharField(max_length=60, unique=True)
    password = CharField(max_length=120)
    class Meta:
        database = db

class Post(Model):
    title = CharField(max_length=120)
    content = TextField()
    photo = CharField(max_length=200)
    class Meta:
        database = db