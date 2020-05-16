from mysqlApp import app

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


