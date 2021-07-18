import peewee

from app.app import db


class User(peewee.Model):
    username = peewee.CharField()
    email = peewee.CharField()
    password = peewee.CharField()
    image = peewee.CharField(max_length=512)


    class Meta:
        database = db