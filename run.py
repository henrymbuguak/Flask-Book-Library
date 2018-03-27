from flask import Flask
from flask_restful import Api
from flask_sqlalchemy import SQLAlchemy
from flask_jwt_extended import JWTManager

app = Flask(__name__)
api = Api(app)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:////tmp/test.db'
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


add_book = []
registered_users = []


import views, models, resources


api.add_resource(resources.UserRegistration, '/api/auth/register')
api.add_resource(resources.UserLogin, '/api/auth/login')
api.add_resource(resources.UserLogoutAccess, '/api/auth/logout')
api.add_resource(resources.UserLogoutRefresh, '/logout/refresh')
api.add_resource(resources.TokenRefresh, '/token/refresh')
api.add_resource(resources.AllUsers, '/users')
api.add_resource(resources.SecretResource, '/secret')
api.add_resource(resources.CreateBook, '/api/books')
api.add_resource(resources.CreateBook, '/api/books/<int:book_id>', endpoint='book_edit')
api.add_resource(resources.CreateBook, '/api/books/<int:book_id>', endpoint='book_delete')
api.add_resource(resources.CreateBook, '/api/books/<int:book_id>', endpoint='book_update')
api.add_resource(resources.GetAllBooks, '/api/books/all', endpoint='retrieve_all_books')
api.add_resource(resources.UserPasswordReset, '/api/auth/reset-password', endpoint='reset_password')
api.add_resource(resources.BorrowBook, '/api/users/books/<bookId>', endpoint='borrow_book')
