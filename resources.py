from flask_restful import Resource, reqparse, request, abort
from models import *
from flask_jwt_extended import (
    create_access_token, create_refresh_token, jwt_required,
    jwt_refresh_token_required, get_jwt_identity, get_raw_jwt
)
from flask import jsonify
from run import add_book, registered_users
import json

parser = reqparse.RequestParser()
parser.add_argument('username', help='This field cannot be blank', required=True)
parser.add_argument('password', help='This field cannot be blank', required=True)


class UserRegistration(Resource):
    def post(self):
        data = parser.parse_args()
        if UserModel.find_by_username(data['username']):
            return {'message': 'Username {} already exist'.format(data['username'])}

        new_user = UserModel(
            username=data['username'],
            password=UserModel.generate_hash(data['password']),
        )
        try:
            # new_user.save_to_db()
            registered_users.append(new_user)
            access_token = create_access_token(identity=data['username'])
            refresh_token = create_refresh_token(identity=data['username'])
            return {
                'message': 'User {} was created'.format(data['username']),
                'access_token': access_token,
                'refresh_token': refresh_token
            }
        except:
            return {'message': 'Something went wrong'}, 500


class UserLogin(Resource):
    def post(self):
        data = parser.parse_args()
        current_user = UserModel.find_by_username(data['username'])
        if not current_user:
            return {'message': 'User {} does not exist'.format(data['username'])}

        if UserModel.verify_hash(data['password'], current_user.password):
            access_token = create_access_token(identity=data['username'])
            refresh_token = create_refresh_token(identity=data['username'])
            return {
                'message': 'You are logged in as {}'.format(current_user.username),
                'access_token': access_token,
                'refresh_token': refresh_token
            }
        else:
            return {'message': 'Wrong password or username'}


class UserLogoutAccess(Resource):
    @jwt_required
    def post(self):
        jti = get_raw_jwt()['jti']
        try:
            revoked_token = RevokedTokenModel(jti=jti)
            revoked_token.add()
            return {'message': 'Access token has been revoked!'}
        except:
            return {'message': 'Something went wrong'}, 500


class UserLogoutRefresh(Resource):
    @jwt_refresh_token_required
    def post(self):
        jti = get_raw_jwt()['jti']
        try:
            revoked_token = RevokedTokenModel(jti=jti)
            revoked_token.add()
            return {'message': 'Refresh token has been revoked!'}
        except:
            return {'message': 'Something went wrong'}, 500


class TokenRefresh(Resource):
    @jwt_refresh_token_required
    def post(self):
        current_user = get_jwt_identity()
        access_token = create_access_token(identity=current_user)
        return {'access_token': access_token}


class UserPasswordReset(Resource):
    def post(self):
        def post(self):
            data = parser.parse_args()
            user = UserModel.find_by_username(data['username'])
            if not user:
                return {'message': 'User {} does not exist'.format(data['username'])}
            return {'message': 'To reset password follow this link'}


class AllUsers(Resource):
    def get(self):
        return jsonify(registered_users=registered_users)
        # return UserModel.return_all()

    def delete(self):
        return UserModel.delete_all()


class SecretResource(Resource):
    @jwt_required
    def get(self):
        return {'answer': 43}


class CreateBook(Resource):
    def post(self):
        data = request.form['title']
        author = request.form['author']
        genre = request.form['genre']
        id = request.form['id']
        add_book.append(data)
        add_book.append(author)
        add_book.append(genre)
        add_book.append(id)
        return {
            'title': data,
            'author': author,
            'genre': genre,
            'id': id
        }

    def get(self, book_id):
        print(add_book)
        return {book_id: add_book[book_id]}

    def put(self, book_id):
        title = request.form['title']
        author = request.form['author']
        genre = request.form['genre']
        id = request.form['id']
        add_book.append(title)
        add_book.append(author)
        add_book.append(genre)
        add_book.append(book_id)
        return {
            'title': title,
            'author': author,
            'genre': genre,
            'id': id
        }

    def delete(self, book_id):
        if book_id not in add_book:
            abort(404, message="Book {} does not exist".format(book_id))
        del add_book[book_id]


class GetAllBooks(Resource):
    def get(self):
        return add_book


class BorrowBook(Resource):
    def post(self, book_id):
        args = parser.parse_args()
        book = {'book': args['book']}
        add_book[book_id] = book
        return add_book
