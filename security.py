#Contain a few important functions
#In memory table of registered users
#Mapping to find the user we are looking for right away and not having to
#Illeterate
from werkzeug.security import safe_str_cmp
from models.user import UserModel


def authenticate(username,password):
    user = UserModel.find_by_username(username)
    if user and safe_str_cmp(user.password,password):
        return user

#Takes in a payload, contents of JWT token
def identity(payload):
    user_id = payload['identity']
    return UserModel.find_by_id(user_id)
