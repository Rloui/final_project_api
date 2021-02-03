from peewee import *
from flask_login import UserMixin

import datetime

DATABASE = PostgresqlDatabase('travel_app')

class BaseModel(Model):
    class Meta:
        database = DATABASE

class Users(UserMixin, BaseModel):
    username = CharField(unique=True)
    email = CharField(unique=True)
    password = CharField()
    join_date = DateTimeField(default=datetime.datetime.now)

class Trip(BaseModel):
    destination = CharField()
    date = DateField()
    budget = CharField()
    created_at = DateTimeField(default=datetime.datetime.now)

class Trip_bridge(BaseModel):
    user_ID = ForeignKeyField(Users)
    trip_ID = ForeignKeyField(Trip)

def initialize():
    DATABASE.connect()
    DATABASE.create_tables([Users, Trip, Trip_bridge], safe=True)
    print('TABLES Created')
    DATABASE.close()

