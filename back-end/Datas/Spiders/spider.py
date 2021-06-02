import requests
import re
from faker import Faker
from Pic_Downloader import Downloader
import time

f = Faker()


def down(url, name):
    ss = Downloader(url, 6, name)
    ss.run()


headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 \
    (KHTML, like Gecko)Chrome/84.0.4147.125 Safari/537.36'}


def baidu(key):
    # name = "dog"
    url = 'https://image.baidu.com/search/flip?tn=baiduimage&ie=utf-8&word=' + key + '&pn=' + str(30)
    res = requests.get(url, headers=headers)
    htlm_1 = res.content.decode()
    links = re.findall('"objURL":"(.*?)",', htlm_1)
    links = [i for i in links if len(i) > 60]
    a = 0
    print(links[:10])
    for i in links[:10]:
        down(i, "../baidu_images/" + key + "/baidu_" + key + "_" + str(a) + ".jpg")
        a += 1
        time.sleep(0.1)


def sougou(key):
    headers = {
        'User_Agent': f.user_agent()
    }
    url = 'https://pic.sogou.com/pics?query=' + key
    html = requests.get(url, headers=headers).content.decode('utf8')
    urls = re.findall('"locImageLink":"(.*?)",', html)
    urls = [i.replace('\\u002F', "/") for i in urls]
    a = 0
    print(urls[:10])
    for i in urls[:10]:
        down(i, "../sogo_images/" + key + "/sogo_" + key + "_" + str(a) + ".jpg")
        a += 1
        time.sleep(0.1)


def qihu(key):
    url = 'https://image.so.com/i?q={0}&src=srp'.format(key)
    html = requests.get(url).content.decode('UTF-8')
    links = re.findall('"thumb_bak":"(.*?)"', html)
    links = [i.replace('\\', '') for i in links]
    print(links[:10])
    a = 0

    for i in links[:10]:
        down(i, "../qihu_images/" + key + "/qihu_" + key + "_" + str(a) + ".jpg")
        a += 1
        time.sleep(0.1)


if __name__ == '__main__':
    import threading
    import os

    key = "hot dog"
    try:
        os.mkdir("../baidu_images/" + key)
        os.mkdir("../qihu_images/" + key)
        os.mkdir("../sogo_images/" + key)
    except:
        pass

    threading.Thread(target=baidu, args=(key,)).start()
    threading.Thread(target=sougou, args=(key,)).start()
    threading.Thread(target=qihu, args=(key,)).start()
