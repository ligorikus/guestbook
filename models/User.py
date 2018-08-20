from peewee import *
import config.db

db = config.db.connect()


class User(Model):
    ROLE_USER  = 0
    ROLE_ADMIN = 1

    email = CharField()
    role = IntegerField(default=0)

    class Meta:
        database = db

