from flask import Flask
app = Flask(__name__)

import time
from datetime import datetime
import socket

@app.route('/')
def hello_world():
    print (datetime.now())
    time.sleep(3)
    return 'Hey, we have Flask in docker container: %s!' % socket.gethostname()

@app.route('/test')
def test_world():
    print (datetime.now())
    #time.sleep(3)
    return 'Hey, we are testing Flask in docker container: %s!' % socket.gethostname()

from random import random
@app.route('/metrics')
def metric_func():
    return 'my_random_metric %f' % random()


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
