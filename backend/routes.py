from flask import Flask, request, render_template

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/upload',methods=['POST'])
def upload_photo():
    file =request.files['photo']
    # 파일 저장 로직 구현
    return 'Photo uploaded!'


