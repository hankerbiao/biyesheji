import requests
from lxml import etree
import re
import time
from Pic_Downloader import Downloader

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.86 Safari/537.36'
}


# 获取全部图片url
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


def down(url, name):
    ss = Downloader(url, 6, "img/Bing_"+name+".jpg")
    ss.run()

# 主函数
def main(key):
    for i in range(0, 120, 35):
        url = 'https://cn.bing.com/images/async?q='+key+'&first=' + str(
            i) + '&count=35&relp=35&scenario=ImageBasicHover&datsrc=N_I&layout=RowBased&mmasync=1'
        img_data = parse_img(url)
        print(img_data)
        a = 0
        for img_url in img_data:
            down(img_url, a)
            a += 1
