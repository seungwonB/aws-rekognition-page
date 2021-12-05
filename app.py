from flask import Flask, render_template, jsonify, request
app = Flask(__name__)
from pymongo import MongoClient
import boto3
client = MongoClient('localhost', 27017) # 내 거
# client = MongoClient('mongodb://test:test@localhost', 27017) # 올릴 때
# db = client.dbrekognition
from collections import Counter
from detect_faces import *
from text import *
from datetime import datetime

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/reko', methods=['POST'])
def rekognition():
    content_receive = request.form['content_give']
    file_receive = request.form['file_give']

    res = photo_analysis(file_receive, content_receive)

    return jsonify({'msg': f'{res}'})

@app.route('/reko_text', methods=['POST'])
def rekognition_text():
    content_receive = request.form['content_give']
    file_receive = request.form['file_give']

    res_text = text_extract(file_receive, content_receive)
    return jsonify({'msg': f'{res_text}'})

if __name__ == '__main__':
    app.run('0.0.0.0', port=5000, debug=True)
