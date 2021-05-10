import requests
from lxml import etree
import re
from faker import Faker
f = Faker()

from Pic_Downloader import Downloader


def down(url, name):
    ss = Downloader(url, 6, "img/sougou_"+str(name)+".jpg")
    ss.run()

def main(key):
    headers = {
        'User_Agent':f.user_agent()
    }
    url = 'https://pic.sogou.com/pics?query=' + key
    html = requests.get(url,headers=headers).content.decode('utf8')
    urls = re.findall('"locImageLink":"(.*?)",',html)
    urls = [i.replace('\\u002F',"/") for i in urls]
    a = 0
    for i in urls[:10]:
        down(i,a)
        a+=1


# print(html)
main('dog')