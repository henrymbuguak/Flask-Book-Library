from flask import Flask
from flask_restful import Api
from flask_sqlalchemy import SQLAlchemy
from flask_jwt_extended import JWTManager

app = Flask(__name__)
api = Api(app)

app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:3918km1990km@localhost/flask'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True
app.config['SECRET_KEY'] = '8ur$*&ebeugxsg%3l1^2^g-(5tfh2+%v#usbb=4h$wemlprv07'


db = SQLAlchemy(app)


@app.before_first_request
def create_tables():
    db.create_all()


app.config['JWT_SECRET_KEY'] = '9ur$*&ebeugxsg%3l1^2^g-(5tfh2+%v#usbb=4h$wemlprv09'
jwt = JWTManager(app)

app.config['JWT_BLACKLIST_ENABLED'] = False
app.config['JWT_BLACKLIST_TOKEN_CHECKS'] = ['access', 'refresh']

@jwt.token_in_blacklist_loader
def check_if_token_in_blacklist(decrypted_token):
    jti = decrypted_token['jti']
    return models.RevokedTokenModel.is_jti_blacklisted(jti)


import views, models, resources

api.add_resource(resources.UserRegistration, '/register')
api.add_resource(resources.UserLogin, '/login')
api.add_resource(resources.UserLogoutAccess, '/logout')
api.add_resource(resources.UserLogoutRefresh, '/logout/refresh')
api.add_resource(resources.TokenRefresh, '/token/refresh')
api.add_resource(resources.AllUsers, '/users')
api.add_resource(resources.SecretResource, '/secret')

