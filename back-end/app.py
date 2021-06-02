import time
import logging as rel_log
import os
import queue
import shutil
from datetime import timedelta
from flask import *
from processor.AIDetector_pytorch import Detector
import time
import core.main
import threading

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


def get_score(score):
    scores = {
        10: 9.0,
        9: 9.1,
        8: 9.2,
        7: 9.3,
        6: 9.4,
        5: 9.5,
        4: 9.6,
        3: 9.7,
        2: 9.8,
        1: 9.9,
        0: 10,
    }

    return float(scores[score])


def ssort(pic_lists):
    new_dict = {}
    for i in pic_lists:
        for key, value in i.items():
            pic_accuracy = key.split('_')[-1]
            final_pic_accuracy = get_score(int(pic_accuracy)) + float(value)
            new_dict[key] = round(float(final_pic_accuracy), 6)
    return sorted(new_dict.items(), key=lambda x: x[1], reverse=True)


@app.route('/test', methods=['GET', 'POST'])
def test():
    key = "hot dog"
    baidu_images = os.listdir("Datas/baidu_images/" + key)
    baidu_image_path = [os.path.join("Datas/baidu_images/" + key, img).replace("\\", "/") for img in baidu_images if
                        img.endswith('jpg')]
    qihu_images = os.listdir("Datas/qihu_images/" + key)
    qihu_images_path = [os.path.join("Datas/qihu_images/" + key, img).replace("\\", "/") for img in qihu_images if
                        img.endswith('jpg')]
    sogo_images = os.listdir("Datas/sogo_images/" + key)
    sogo_image_path = [os.path.join("Datas/sogo_images/" + key, img).replace("\\", "/") for img in sogo_images if
                       img.endswith('jpg')]
    # all_picutrues = baidu_image_path + qihu_images_path + sogo_image_path
    all_picutrues = baidu_image_path

    pic_accuracy_list = core.main.c_main(
        all_picutrues, current_app.model, "jpg")

    finall_sort_picslist = ssort(pic_accuracy_list)  # 排序后的结果

    for index, value in enumerate(finall_sort_picslist):
        accuracy = value[1]
        pic_name = value[0].split("_")[0]  # 拿到网站名字 百`度 搜狗 360
        pic_id = value[0].split(".")[0].split('_')[1]  # 图片编号 0 - 10

        print("{}.在 {} 排名第 {} 的图片，在联合排序算法中排名第 {} , 权值为：{}".format(index + 1, pic_name, pic_id, index + 1, accuracy))

    pic_urls = []

    for i in finall_sort_picslist:
        pic_urls.append(i[0])

    pic_urls_ = ["http://127.0.0.1:5003/tmp/ct/" + i + ".jpg" for i in pic_urls]
    draw_urls = ["http://127.0.0.1:5003/tmp/draw/" + i + ".jpg" for i in pic_urls]

    finall_pics = []
    for i in range(len(pic_urls)):
        pic_info = {}
        pic_info['origin_pics'] = pic_urls_[i]
        pic_info['draw_pics'] = ["".join(draw_urls[i])]
        pic_info['pic_name'] = [i.split('/')[-1] for i in pic_urls]
        finall_pics.append(pic_info)

    return jsonify({'status': 1,
                    'image_url': finall_pics})


@app.route('/')
def hello_world():
    return redirect(url_for('static', filename='./index.html'))


# show photo
@app.route('/tmp/<path:file>', methods=['GET'])
def show_photo(file):
    if request.method == 'GET':
        file = file.replace('.jpg.jpg', ".jpg")
        if not file is None:
            if file.find('draw/http://127.0.0.1:5003') > -1:
                file = file.split('/')[-2:]
                file = file[0] + "/" + file[1]
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
