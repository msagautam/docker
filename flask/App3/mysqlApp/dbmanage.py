from flask_sqlalchemy import SQLAlchemy

from mysqlApp import app
app.config['SQLALCHEMY_DATABASE_URI'] = "mysql+pymysql://root:testpassword@172.18.0.2/testdb"
app.config['SQLALCHEMY_ECHO'] = True; #Debugging Enabled
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

from .dbmodels import User

db.init_app(app)


import socket
@app.route('/')
def home():
    return 'Hey, we have Flask in docker container: %s!\n' % socket.gethostname()

@app.route('/test')
def test_world():
    return 'Hey, we are testing Flask in docker container: %s!\n' % socket.gethostname()

from random import random
@app.route('/metrics')
def metric_func():
    return 'my_random_metric %f\n' % random()


#with app.app_context():

@app.route('/createdb')
def create_db_tables():
    db.create_all() # Create database tables for our data models
    return "db tables successfully created"

from flask import request
@app.route('/adduser', methods=['GET'])
def create_user():
    """Create a user."""
    username = request.args.get('user')
    email = request.args.get('email')
    if username and email:
        new_user = User(username=username, email=email);
        db.session.add(new_user)  # Adds new User record to database
        db.session.commit()  # Commits all changes
        return "%s successfully created!" % new_user
