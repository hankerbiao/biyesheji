import threading
import requests
import re
from faker import Faker
from lxml import etree

f = Faker()

from Pic_Downloader import Downloader


def down(url, name, webname):
    ss = Downloader(url, 6, "img/{0}_".format(webname) + str(name) + ".jpg")
    ss.run()


headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.125 Safari/537.36'}


def baidu(key):
    # name = "dog"
    url = 'https://image.baidu.com/search/flip?tn=baiduimage&ie=utf-8&word=' + key + '&pn=' + str(30)
    res = requests.get(url, headers=headers)
    htlm_1 = res.content.decode()
    links = re.findall('"objURL":"(.*?)",', htlm_1)
    links = [i for i in links if len(i) > 60]
    a = 0
    for i in links[:10]:
        down(i, a, "baidu")
        a += 1


def sougou(key):
    headers = {
        'User_Agent': f.user_agent()
    }
    url = 'https://pic.sogou.com/pics?query=' + key
    html = requests.get(url, headers=headers).content.decode('utf8')
    urls = re.findall('"locImageLink":"(.*?)",', html)
    urls = [i.replace('\\u002F', "/") for i in urls]
    a = 0
    for i in urls[:10]:
        down(i, a, "sougou")
        a += 1


def qihu(key):
    url = 'https://image.so.com/i?q={0}&src=srp'.format(key)
    html = requests.get(url).content.decode('UTF-8')
    links = re.findall('"thumb_bak":"(.*?)"', html)
    links = [i.replace('\\', '') for i in links]
    print(links)
    print(len(links))
    a = 0
    for i in links[:10]:
        down(i, a, "qihu")
        a += 1


def parse_img(url):
    response = requests.get(url, headers=headers)
    response.encoding = response.apparent_encoding
    data = response.content.decode('utf-8', 'ignore')
    html = etree.HTML(data)
    conda_list = html.xpath('//a[@class="iusc"]/@m')
    all_url = []  # 用来保存全部的url
    for i in conda_list:
        img_url = re.search('"murl":"(.*?)"', i).group(1)
        all_url.append(img_url)
    return all_url


def biying(key):
    for i in range(0, 120, 35):
        url = 'https://cn.bing.com/images/async?q=' + key + '&first=' + str(
            i) + '&count=35&relp=35&scenario=ImageBasicHover&datsrc=N_I&layout=RowBased&mmasync=1'
        img_data = parse_img(url)
        print(img_data)
        a = 0
        for img_url in img_data:
            down(img_url, a, "biying")
            a += 1


if __name__ == '__main__':
    import threading
    key = "狗"
    threading.Thread(target=baidu, args=(key,)).start()
    threading.Thread(target=sougou,
                     args=(key,)).start()
    # threading.Thread(target=biying, args=(key,)).start()
    threading.Thread(target=qihu, args=(key,)).start()
