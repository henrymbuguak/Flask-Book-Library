# Flask-Book-Library [![Build Status](https://travis-ci.org/henrymbuguak/Flask-Book-Library.svg?branch=master)](https://travis-ci.org/henrymbuguak/Flask-Book-Library) [![Maintainability](https://api.codeclimate.com/v1/badges/92de23a6ec9740be5cf3/maintainability)](https://codeclimate.com/github/henrymbuguak/Flask-Book-Library/maintainability)

This a flask restful api created using flask web framework to management books as I learn to 
become a better software developer.

### Project setup

This project is using python3.6 and you need to create a virtual environment by running the
following command: 

<code>virtualenv -p /usr/bin/python3.6 my_project</code>

You can use also virtualenvwrapper.

###### Clone the project

To get the project run the following command:

<code>git clone https://github.com/henrymbuguak/Flask-Book-Library.git</code>

###### Installing dependencies

To install dependencies <b>cd Flask-Book-Library</b> and make sure your virtual environment
is active. run the following command:

<code>pip install -r requirements.txt</code>

##### To run the Project use this command

<code>FLASK_APP=run.py FLASK_DEBUG=1 flask run</code>


##### To test Endpoints Using Postman

This are the endpoint I have today:

* show all books and create book:  /api/books
* Edit book:  /api/books/<int:book_id>
* delete a book:  /api/books/<int:book_id>
* user register: /api/auth/register
* user login: /api/auth/login
* user logout: /api/auth/logout


###### Basic test

Have a look at test_basic.py file to see how I am approaching unit test

To run the test run the following command: <code>python -m unittest discover</code>

##### Heroku Url

https://hmbucket-api-heroku.herokuapp.com/
