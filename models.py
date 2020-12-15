from peewee import *

import datetime

DATABASE = PostgresqlDatabase('trips')

class Trips(Model):
    destination = CharField()
    date = DateTimeField()
    budget = CharField()
    created_at = DateTimeField(default=datetime.datetime.now)

    class Meta:
        database = DATABASE

def ininialize():
    DATABASE.connect()
    DATABASE.create_tables([Trips], safe=True)
    print('TABLES Created')
    DATABASE.close()