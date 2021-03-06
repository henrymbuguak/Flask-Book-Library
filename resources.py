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

user_details = {'username': ["henry@gmail.com", 'henry@gmail.com'], 'obola': ["henryk@gmail.com", 'henry@gmail.com'],
                'leslie': ["henrym@gmail.com", 'henry@gmail.com'],
                'henry': ["henry@gmail.com", 'henry@gmail.com']}

books = []

new_books = {'id': 1}


class UserRegister(Resource):
    def post(self):
        username = request.form['username']
        password = request.form['password']
        registered_users.append(username)
        registered_users.append(password)
        access_token = create_access_token(identity=['username'])
        return {
            'username': username,
            'access_token': access_token
        }


class UserLogin(Resource):
    def post(self):
        username= request.form['username']
        password= request.form['password']
        current_user = username in registered_users
        print(current_user)
        if not current_user:
            return {'message': 'User does not exist'}
        return {
            'message': 'You are logged in as {}',
        }


class UserLogout(Resource):
    def post(self):
        return {
            'message': 'logout successfully'
        }


class AllUsers(Resource):
    def get(self):
        return jsonify(registered_users=registered_users)


class CreateBook(Resource):
    def post(self):
        data = request.form['title']
        author = request.form['author']
        genre = request.form['genre']
        id = request.form['id']
        for entry in data, author, genre, id:
            book = {'id': int(id), 'author': author, 'genre': genre, 'title': data}
            books.append(book)
            return books

    def get(self, book_id):
        print(add_book)
        return {book_id: add_book[book_id]}

    def put(self, book_id):
        books['id'] = book_id
        title = request.form['title']
        author = request.form['author']
        genre = request.form['genre']
        books['title']=title
        books['author']=author
        books['genre']=genre
        return {
            'title': title,
            'author': author,
            'genre': genre,
            'id': id
        }

    def delete(self, book_id):
        key = 'id'
        if key in new_books.keys():
            new_books.pop(key)
            return {
                'message': 'book deleted successfully'
            }
        else:
            return {
                'message': 'Book with that id not found'
            }


class GetAllBooks(Resource):
    def get(self):
        return books


class BorrowBook(Resource):
    def post(self, book_id):

        return add_book


class UserPasswordReset(Resource):

    def post(self):
        username = request.form['username']
        email = user_details['username']
        if username == email[0]:
            return {
                'message': 'reset password here'
            }
        else:
            return {
                'message': 'There is no user with that username'
            }
