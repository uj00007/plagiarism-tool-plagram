from mongoengine import *

from signup.models import User

connect("plagram")
print(User.objects)
list=[]
for user in User.objects:
    list.append(user.username)
    print(user.password)

print(list)