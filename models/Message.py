from peewee import *
import config.db
from models.User import User

db = config.db.connect()


class Message(Model):
    user = ForeignKeyField(User, related_name='messages')
    message = CharField()

    class Meta:
        database = db
