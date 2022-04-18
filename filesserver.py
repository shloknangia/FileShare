#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# author: shloknangia@gmail.com
# desc: a file share(upload/download) server

import os
import time

from flask import Flask, request, redirect, url_for, render_template, jsonify, send_file
from werkzeug.utils import secure_filename

WORK_DIR = os.getcwd()
UPLOAD_FOLDER = WORK_DIR #+ '/uploads'
ALLOWED_EXTENSIONS = set(['txt', 'zip', 'tar.gz', 'rar', 'xlsx'])

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
app.config['MAX_CONTENT_LENGTH'] = 1024 * 1024 * 1024  # 1G


def allowed_file(filename):
    return True
    # return '.' in filename and filename.rsplit('.', 1)[1] in ALLOWED_EXTENSIONS


def human_filesize(size):
    """ Readable file size """
    if size < 1024:
        return '%d B' % size
    if size < 1024 * 1024:
        return "%.1f K" % (size / 1024)
    if size < 1024 * 1024 * 1024:
        return "%.1f M" % (size / 1024 / 1024)
    if size < 1024 * 1024 * 1024 * 1024:
        return "%.1f G" % (size / 1024 / 1024 / 1024)
    return '%d B' % size

@app.route('/')
@app.route('/<path>')
def index(path=None):
    """ file list display """
    file_list = []
    if(path == None):
        FOLDER_PATH = UPLOAD_FOLDER
    else:
        FOLDER_PATH =  UPLOAD_FOLDER + "/" + path    
    # FOLDER_PATH = (path == None) ? UPLOAD_FOLDER: UPLOAD_FOLDER + "/" + path
    files = [f for f in os.listdir(FOLDER_PATH)]
    # Sort in reverse chronological order
    files.sort(key=lambda x: os.path.getmtime(FOLDER_PATH + "/" + x), reverse=True)

    for filename in files:
        st = os.stat(FOLDER_PATH + "/" + filename)
        file_vo = {
            'filename': filename,
            'size': human_filesize(st.st_size),
            'mtime': time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(st.st_mtime)),
        }
        file_list.append(file_vo)
    return render_template("index.html", file_list=file_list)


@app.route('/download_file/<filename>')
def download_file(filename=None):
    """ download file """
    if filename is None:
        return "404"
    try:
        return send_file(UPLOAD_FOLDER + "/" + filename, as_attachment=True)
    except Exception as e:
        return "404"


@app.route('/upload_file', methods=['GET', 'POST'])
def upload_file():
    """ File Upload """
    if request.method == 'POST':
        file = request.files['file']
        if file and allowed_file(file.filename):
            # filename = secure_filename(file.filename) 
            filename = file.filename.replace(' ', '')
            save_path = os.path.join(app.config['UPLOAD_FOLDER'], filename)
            file.save(save_path)
    return redirect(url_for('index'))


@app.route('/test', methods=['GET', 'POST'])
def test():
    pass

if __name__ == "__main__":
    # server start up
    app.run(host='0.0.0.0', port=8080, debug=True)

