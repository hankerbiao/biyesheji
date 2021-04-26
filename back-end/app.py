import datetime
import logging as rel_log
import os
import shutil
from datetime import timedelta
from flask import *
from processor.AIDetector_pytorch import Detector
import time
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


def ssort(list):
    new_dict = {}
    for i in list:
        new_dict.update(i)
    return sorted(new_dict.items(), key=lambda x: x[1], reverse=True)


@app.route('/test', methods=['GET', 'POST'])
def test():
    baidu_images = os.listdir("Spider/baidu_images")
    baidu_image_path = [os.path.join("Spider/baidu_images", img).replace("\\", "/") for img in baidu_images]
    qihu_images = os.listdir("Spider/qihu_images")
    qihu_images_path = [os.path.join("Spider/qihu_images", img).replace("\\", "/") for img in qihu_images]
    sogo_images = os.listdir("Spider/sogo_images")
    sogo_image_path = [os.path.join("Spider/sogo_images", img).replace("\\", "/") for img in sogo_images]
    all_picutrues = baidu_image_path + qihu_images_path + sogo_image_path

    pic_accuracy_list = []  # 最终所有图片保存的列表
    for img in all_picutrues:
        try:
            pic_accuracy = dict()
            input_key = "dog"  # 前端输入的关键字
            pid, image_info = core.main.c_main(
                img, current_app.model, "jpg")

            print("=" * 100)
            if len(image_info) == 1:
                print("{0}图中共识别出{1}种".format(pid, len(image_info)))
                for key, value in image_info.items():
                    Accuracy = float(value[1])
                    pic_accuracy[pid] = Accuracy  # 图片的名称和对应的准确率
                    print(pic_accuracy)
                    pic_accuracy_list.append(pic_accuracy)

            if len(image_info) > 1:  # 如果图中有多条狗
                many_pic_accuracy = {}
                tmp_dict = {}
                for key, value in image_info.items():
                    many_pic_accuracy[key] = float(value[1])
                # 按值排序字典，拿到多图中准确率最高的图
                a = sorted(many_pic_accuracy.items(), key=lambda x: x[1], reverse=True)
                tmp_v = a[0][1]
                tmp_dict[pid] = tmp_v
                pic_accuracy_list.append(tmp_dict)
        except Exception as e:
            print(e)
            continue

    finall_sort_picslist = ssort(pic_accuracy_list)  # 排序后的结果

    for index, value in enumerate(finall_sort_picslist):
        accuracy = value[1]
        pic_name = value[0].split("_")[0]  # 拿到网站名字 百度 搜嘎 360
        pic_id = value[0].split(".")[0].split('_')[1]  # 图片编号 0 - 10
        print("{}.在 {} 排名第 {} 的图片，在yolo算法中排名第 {} , 准确率为：{}".format(index + 1, pic_name, pic_id, index + 1, accuracy))

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
        print("current_app:", current_app)

    app.run(host='127.0.0.1', port=5003, debug=True)
