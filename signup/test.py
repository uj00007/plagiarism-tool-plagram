from mongoengine import *

from signup.models import User

connect("plagram")

for user in User.objects:
    print(user.password)