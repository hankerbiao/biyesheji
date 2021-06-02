import requests
import re
from Pic_Downloader import Downloader
from faker import Faker

f = Faker()


def down(url, name):
    ss = Downloader(url, 6, "img/baidu_" + str(name) + ".jpg")
    ss.run()


def main(key):
    headers = {
        'Host': 'image.baidu.com',
        'Referer': 'https://image.baidu.com/',
        'User-Agent': f.user_agent(),
    }
    url = 'https://image.baidu.com/search/flip?tn=baiduimage&ie=utf-8&word=' + key + '&pn=' + str(30)
    res = requests.get(url, headers=headers)
    htlm_1 = res.content.decode()
    links = re.findall('"objURL":"(.*?)",', htlm_1)
    links = [i for i in links if len(i) > 60]
    a = 0

    for i in links:
        down(i, a)
        a += 1


main("dog")
