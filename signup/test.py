from mongoengine import *
from passlib.handlers.sha2_crypt import sha256_crypt

from signup.models import User

connect("plagram")
v="$2b$14$KVW3gTQR3RVllCp9Xqno1..fjln19MxP.FTxTD7FoESEQ6yOPF2g6"
print(User.objects)
list=[]
for user in User.objects:
    list.append(user.password)
    print(user.password)
    if v in user.password:
        print("yayy")

print(list)

hash = sha256_crypt.encrypt("ujjwal")
print(hash)

hash2 = sha256_crypt.encrypt("ujjwal")
print(hash2)