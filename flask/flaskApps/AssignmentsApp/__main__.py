from flask import Flask
app = Flask(__name__)

import time
from datetime import datetime

@app.route('/')
def hello_world():
    print (datetime.now())
    time.sleep(3)
    return 'Hey, we have Flask in a Docker container!'

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
