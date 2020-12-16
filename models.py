from peewee import *
from flask_login import UserMixin

import datetime

DATABASE = PostgresqlDatabase('travel_app')

class Users(UserMixin, Model):
    username = CharField(unique=True)
    email = CharField(unique=True)
    password = CharField()

    class Meta:
        database = DATABASE


class Trip(Model):
    destination = CharField()
    date = DateField()
    budget = CharField()
    created_at = DateTimeField(default=datetime.datetime.now)

    class Meta:
        database = DATABASE

def initialize():
    DATABASE.connect()
    DATABASE.create_tables([Users, Trip], safe=True)
    print('TABLES Created')
    DATABASE.close()