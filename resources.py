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

        return add_book
