import requests
from Pic_Downloader import Downloader

import re


def down(url, name):
    ss = Downloader(url, 6, "Spider/img/360_" + str(name) + ".jpg")
    ss.run()


def main(key):
    url = 'https://image.so.com/i?q={0}&src=srp'.format(key)
    html = requests.get(url).content.decode('UTF-8')
    links = re.findall('"thumb_bak":"(.*?)"', html)
    links = [i.replace('\\', '') for i in links]
    print(links)
    print(len(links))
    a = 0
    for i in links[:10]:
        down(i, a)
        a += 1
