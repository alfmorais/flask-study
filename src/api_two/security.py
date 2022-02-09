from user import User
from werkzeug.security import safe_str_cmp

users = [
    User(1, "joaquim", "1234"),
]

username_mapping = {
    user.username: user for user in users  # list comprehension
}

userid_mapping = {
    user.id: user for user in users  # list comprehension
}


def authenticate(username, password):
    user = username_mapping.get(username, None)
    if user and safe_str_cmp(user.password, password):
        return user


def identity(payload):
    user_id = payload["identity"]
    return userid_mapping.get(user_id, None)
