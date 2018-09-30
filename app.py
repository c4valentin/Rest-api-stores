#201 means something was created
#202 means the creating is being delayed
#JWT json web token

from flask import Flask
from flask_restful import Api
from flask_jwt import JWT
from security import authenticate, identity
from resources.user import UserRegister
from resources.item import Item,ItemList
from resources.store import Store,StoreList

app = Flask(__name__)

#root foler in our project, can be mysql whatever you want
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///data.db'

#so sqlAlchemy doesn't track every change made to the sqlAlchemy made to a sesson
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

app.secret_key = 'jose'
api = Api(app)

#creates a new endpoint # /auth send it to username password
jwt = JWT(app,authenticate,identity)

api.add_resource(Store, '/store/<string:name>')
api.add_resource(Item, '/item/<string:name>')
api.add_resource(ItemList,'/items')
api.add_resource(StoreList, '/stores')

api.add_resource(UserRegister, '/register')

#Circular imports
if __name__ == '__main__':
    from db import db
    db.init_app(app)
    app.run(port =5000, debug=True)
