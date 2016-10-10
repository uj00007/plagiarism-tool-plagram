from django.db import models
from mongoengine import *

connect('plagram')


class User(Document):
    email = StringField(required=True)
    name = StringField(max_length=50,required=True)
    username = StringField(max_length=50,required=True)
    photo=FileField
    password=StringField(required=True)
