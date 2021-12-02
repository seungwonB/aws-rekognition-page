from flask import Flask, render_template, jsonify, request
app = Flask(__name__)
from pymongo import MongoClient
import boto3
client = MongoClient('localhost', 27017) # 내 거
# client = MongoClient('mongodb://test:test@localhost', 27017) # 올릴 때
db = client.dbsparta_plust_week1
from collections import Counter
from detect_faces import *
from datetime import datetime

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/diary', methods=['GET'])
def show_diary():
    diaries = list(db.diary.find({}, {'_id': False}))
    return jsonify({'all_diary': diaries})

@app.route('/diary', methods=['POST'])
def save_diary():
    title_receive = request.form['title_give']
    content_receive = request.form['content_give']
    file = request.files["file_give"]

    extension = file.filename.split(".")[-1]

    today = datetime.now()
    mytime = today.strftime('%Y-%m-%d-%H-%M-%S') # 올라간 사진 이름
    mytime2 = today.strftime('%Y.%m.%d') # 올린 사진 날짜 표시

    filename = f'file-{mytime}'
    timename = f'{mytime2}'
    save_to = f'static/{filename}.{extension}'
    file.save(save_to)

    doc = {
        'title': title_receive,
        'content': content_receive,
        'file': f'{filename}.{extension}',
        'time': f'{timename}'
    }

    db.diary.insert_one(doc)

    return jsonify({'msg': doc['file']})

@app.route('/reko', methods=['POST'])
def rekognition():
    content_receive = request.form['content_give']
    file_receive = request.form['file_give']

    res = photo_analysis(file_receive, content_receive)

    # return jsonify({'msg': f'{content_receive}, {file_receive}'})
    return jsonify({'msg': f'{res}'})

if __name__ == '__main__':
    app.run('0.0.0.0', port=5000, debug=True)
