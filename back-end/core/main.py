from core import process, predict
import time
import queue
import threading

names = ['person', 'bicycle', 'car', 'motorcycle', 'airplane', 'bus', 'train', 'truck', 'boat', 'traffic light',
         'fire hydrant', 'stop sign', 'parking meter', 'bench', 'bird', 'cat', 'dog', 'horse', 'sheep', 'cow',
         'elephant', 'bear', 'zebra', 'giraffe', 'backpack', 'umbrella', 'handbag', 'tie', 'suitcase', 'frisbee',
         'skis', 'snowboard', 'sports ball', 'kite', 'baseball bat', 'baseball glove', 'skateboard', 'surfboard',
         'tennis racket', 'bottle', 'wine glass', 'cup', 'fork', 'knife', 'spoon', 'bowl', 'banana', 'apple',
         'sandwich', 'orange', 'broccoli', 'carrot', 'hot dog', 'pizza', 'donut', 'cake', 'chair', 'couch',
         'potted plant', 'bed', 'dining table', 'toilet', 'tv', 'laptop', 'mouse', 'remote', 'keyboard', 'cell phone',
         'microwave', 'oven', 'toaster', 'sink', 'refrigerator', 'book', 'clock', 'vase', 'scissors', 'teddy bear',
         'hair drier', 'toothbrush']

pic_accuracy_list = []


def predict_pics(path, model, ext):
    pic_accuracy = dict()
    image_data = process.pre_process(path)
    image_info = predict.predict(image_data, model, ext)
    pid = image_data[1]
    print(image_info)

    if len(image_info) == 0:
        print("=" * 100)
        print({pid: 0.0})
        pic_accuracy_list.append({pid: 0.0})
        print("=" * 100)

    if len(image_info) == 1:
        # 如果只有图中只有一种
        for key, value in image_info.items():
            Accuracy = float(value[1])
            pic_accuracy[pid] = Accuracy  # 图片的名称和对应的准确率
            pic_accuracy_list.append(pic_accuracy)

    if len(image_info) > 1:  # 如果图中有多种
        many_pic_accuracy = {}
        tmp_dict = {}
        for key, value in image_info.items():
            many_pic_accuracy[key] = float(value[1])
        # 按值排序字典，拿到多图中准确率最高的图
        a = sorted(many_pic_accuracy.items(), key=lambda x: x[1], reverse=True)
        tmp_v = a[0][1]
        tmp_dict[pid] = tmp_v
        pic_accuracy_list.append(tmp_dict)


def c_main(path, model, ext):
    q = queue.Queue()

    for i in path:
        q.put(i)
    while q.qsize() != 0:
        img = q.get()
        threading.Thread(target=predict_pics, args=(img, model, ext)).start()
        time.sleep(0.4)
    time.sleep(1)

    return pic_accuracy_list
