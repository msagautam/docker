from myfilesApp import app

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

from flask import render_template
@app.route('/upload')
def file_uploader():
    return render_template('fileuploader.html')

from flask import request
@app.route('/myuploader', methods = ['GET', 'POST'])
def upload_file():
    if request.method == 'POST':
        f = request.files['file']
        f.save(f.filename)
        return 'file uploaded successfully'
    return 'file uploaded unsuccessful!'
