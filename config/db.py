from peewee import MySQLDatabase


def connect():
    db = MySQLDatabase(
        host='localhost',
        user='ligo',
        password='1',
        database='guestbook'
    )
    db.connect()

    return db
