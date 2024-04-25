import json
from taskite.models import User

f = open("users.json")

users = json.load(f)

for user in users:
    new_user = User(**user)
    new_user.set_password('password')
    new_user.is_verified = True
    new_user.save()
