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
def upload_dropzone():
    return render_template('dropzone.html')

@app.route('/uppy')
def upload_uppy():
    return render_template('uppy.html')


from flask import request,jsonify
from werkzeug.utils import secure_filename
import os
UPLOAD_FOLDER = '/var/www/upload_data_files/'
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

ALLOWED_EXTENSIONS = set(['png', 'jpg', 'jpeg', 'gif'])
def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

@app.route('/myuploader', methods = ['POST'])
def upload_file():
    if request.method == 'POST':
        # check if the post request has the file part
        print(request.files)
        if len(request.files) == 0:
            return jsonify(
                error="No file in request"
            ), 400
        for fi in request.files:
            f = request.files[fi]
            print("All files: %s" % f.filename)

        for fi in request.files:
            f = request.files[fi]
            print("file: %s" % f.filename)
            if f and allowed_file(f.filename):
                filename = secure_filename(f.filename)
                f.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
                return jsonify(
                    message="ok"
                ), 201
        return jsonify(
            error="File in request is not a valid type"
        ), 400

