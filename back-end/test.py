# -*- coding: utf-8 -*-

import tkinter as tk
import threading
import requests
import random
from hashlib import md5


def make_md5(s, encoding='utf-8'):
    return md5(s.encode(encoding)).hexdigest()


appid = '20200502000436928'
appkey = 'tc3FMcltqCcUYm9GgJRB'
endpoint = 'http://api.fanyi.baidu.com'
path = '/api/trans/vip/translate'
url = endpoint + path


def trans(from_lang, to_lang, query):
    res = ""
    salt = random.randint(32768, 65536)
    sign = make_md5(appid + query + str(salt) + appkey)
    headers = {'Content-Type': 'application/x-www-form-urlencoded'}
    payload = {'appid': appid, 'q': query, 'from': from_lang, 'to': to_lang, 'salt': salt, 'sign': sign}
    r = requests.post(url, params=payload, headers=headers)
    result = r.json()['trans_result']
    for i in result:
        res += i['dst'] + "\n"
    return res.strip()


def trans_main1(query):
    """zh-kor-en"""
    zh2kor_res = trans('zh', 'kor', query)
    kor2en_res = trans('kor', 'en', zh2kor_res)
    en2zh_res = trans('en', 'zh', kor2en_res)
    return en2zh_res


def trans_main2(query):
    """zh-de-jp"""
    zh2de_res = trans('zh', 'de', query)
    de2jp_res = trans('de', 'jp', zh2de_res)
    jp2zh_res = trans('jp', 'zh', de2jp_res)
    return jp2zh_res


def trans_main3(query):
    """zh-fra"""
    zh2de_res = trans('zh', 'fra', query)
    de2jp_res = trans('fra', 'zh', zh2de_res)
    return de2jp_res


root = tk.Tk()
root.geometry('600x800+300+200')
root.title("论文降重助手-城建417")
text_1 = tk.Text(root, height=8, width=58, font=("微软雅黑", 16))
text_1.place(x=10, y=10)
text_1.insert("insert", "这里输入原文\n\n论文降重助手，在不改变原文意思的条件下，改变原文内容，人工简单修改一下即可达到降重的目的")

button2 = tk.Button(root, text="赞助", font=("微软雅黑", 5))
button2.place(x=500, y=750)

text_2_1 = tk.Text(root, height=8, width=58, font=("微软雅黑", 16))
text_2_1.place(x=10, y=250)
text_2_1.insert("insert", "结果一")

text_2_2 = tk.Text(root, height=8, width=58, font=("微软雅黑", 16))
text_2_2.place(x=10, y=410)
text_2_2.insert("insert", "结果二")

text_2_3 = tk.Text(root, height=8, width=58, font=("微软雅黑", 16))
text_2_3.place(x=10, y=570)
text_2_3.insert("insert", "结果三")

lock = threading.Lock()


def main():
    query = text_1.get("1.0", "end")
    text1 = trans_main1(query)
    text2 = trans_main2(query)
    text3 = trans_main3(query)

    text_2_1.insert("insert", text1)
    text_2_2.insert("insert", text2)
    text_2_3.insert("insert", text3)


def clear():
    text_1.delete(1.0, tk.END)
    text_2_1.delete(1.0, tk.END)
    text_2_2.delete(1.0, tk.END)
    text_2_3.delete(1.0, tk.END)


button = tk.Button(root, text="给我转！", height=2, width=5, font=("微软雅黑", 20), command=main)
button.place(x=320, y=180)

button_clear = tk.Button(root, text="清空内容", height=2, width=5, font=("微软雅黑", 20),command=clear)
button_clear.place(x=120, y=180)

label = tk.Label(root,text="论文降重软件，三元一个，十元三个～",font=("微软雅黑",20),fg="red")
label.place(x=20,y=740)


root.mainloop()
