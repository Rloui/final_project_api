from peewee import *

import datetime

DATABASE = PostgresqlDatabase('travel_app')

class Trip(Model):
    destination = CharField()
    date = DateField()
    budget = DecimalField()
    created_at = DateTimeField(default=datetime.datetime.now)

    class Meta:
        database = DATABASE

def initialize():
    DATABASE.connect()
    DATABASE.create_tables([Trip], safe=True)
    print('TABLES Created')
    DATABASE.close()