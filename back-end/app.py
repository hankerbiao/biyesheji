import datetime
import logging as rel_log
import os
import shutil
from datetime import timedelta
from flask import *
from processor.AIDetector_pytorch import Detector

import core.main


UPLOAD_FOLDER = r'./uploads'

ALLOWED_EXTENSIONS = set(['png', 'jpg'])
app = Flask(__name__)
app.secret_key = 'secret!'
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

werkzeug_logger = rel_log.getLogger('werkzeug')
werkzeug_logger.setLevel(rel_log.ERROR)

# 解决缓存刷新问题
app.config['SEND_FILE_MAX_AGE_DEFAULT'] = timedelta(seconds=1)


# 添加header解决跨域
@app.after_request
def after_request(response):
    response.headers['Access-Control-Allow-Origin'] = '*'
    response.headers['Access-Control-Allow-Credentials'] = 'true'
    response.headers['Access-Control-Allow-Methods'] = 'POST'
    response.headers['Access-Control-Allow-Headers'] = 'Content-Type, X-Requested-With'
    return response


def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1] in ALLOWED_EXTENSIONS


@app.route('/test', methods=['GET', 'POST'])
def test():

    images = os.listdir("Spider/img")
    for img in images:
        image_path = os.path.join("Spider/img",img).replace("\\","/")
        try:
            pid, image_info = core.main.c_main(
                image_path, current_app.model, "jpg")
            for key,value in image_info.items():
                print(img.replace(".jpg","")+"_"+key + " 的概率:" + str(round(value[1] * 100, 4)) + "%")
        except Exception as e:
            print(e)
            continue

    pid = "111"
    image_info = {
        'msg': 'Hello, Python !'
    }

    return jsonify({'status': 1,
                    'image_url': 'http://127.0.0.1:5003/tmp/ct/' + pid,
                    'draw_url': 'http://127.0.0.1:5003/tmp/draw/' + pid,
                    'image_info': image_info})


@app.route('/')
def hello_world():
    return redirect(url_for('static', filename='./index.html'))

@app.route('/upload', methods=['GET', 'POST'])
def upload_file():
    # file = request.files['file']
    # if file and allowed_file(file.filename):
        # src_path = os.path.join(app.config['UPLOAD_FOLDER'], file.filename)
        # file.save(src_path)
        # shutil.copy(src_path, './tmp/ct')
    imgs = os.listdir("tmp/ct")
    # print("imgs",imgs)
    for img in imgs:
        try:
            if img.find("jpg") == -1:
                continue
            image_path = os.path.join('./tmp/ct', img)
            # print("image_path",image_path)
            pid, image_info = core.main.c_main(
                image_path, current_app.model, "jpg")
            # print("pid",pid)
            print("image",image_info)
        except:
            print("出错啦：",img)
    # return jsonify({'status': 1,
    #                 'image_url': 'http://127.0.0.1:5003/tmp/ct/' + pid,
    #                 'draw_url': 'http://127.0.0.1:5003/tmp/draw/' + pid,
    #                 'image_info': image_info})


    return jsonify({'status': 0})


@app.route("/download", methods=['GET'])
def download_file():
    # 需要知道2个参数, 第1个参数是本地目录的path, 第2个参数是文件名(带扩展名)
    return send_from_directory('data', 'testfile.zip', as_attachment=True)

# show photo
@app.route('/tmp/<path:file>', methods=['GET'])
def show_photo(file):
    if request.method == 'GET':
        if not file is None:
            image_data = open(f'tmp/{file}', "rb").read()
            response = make_response(image_data)
            response.headers['Content-Type'] = 'image/png'
            return response


if __name__ == '__main__':
    files = [
        'uploads', 'temp/ct', 'temp/draw',
        'temp/image', 'temp/mask', 'temp/uploads'
    ]
    for ff in files:
        if not os.path.exists(ff):
            os.makedirs(ff)
    with app.app_context():
        current_app.model = Detector()
        print("current_app:",current_app)

    app.run(host='127.0.0.1', port=5003, debug=True)
