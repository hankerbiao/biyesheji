import requests
import re
from Pic_Downloader import Downloader


def down(url, name):
    ss = Downloader(url, 6, "img/baidu_"+str(name)+".jpg")
    ss.run()


def main(key):
    headers = {'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.125 Safari/537.36'}
    # name = "dog"
    url = 'https://image.baidu.com/search/flip?tn=baiduimage&ie=utf-8&word='+key+'&pn='+str(30)
    res = requests.get(url,headers=headers)
    htlm_1 = res.content.decode()
    links = re.findall('"objURL":"(.*?)",',htlm_1)
    links = [i for i in links if len(i) > 60]
    a = 0
    print(len(links))
    for i in links:
        down(i,a)
        a+=1
main("dog")