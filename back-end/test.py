ll = [{'baidu_2.jpg': 0.82}, {'baidu_3.jpg': 0.702}, {'baidu_4.jpg': 0.824}, {'baidu_5.jpg': 0.785}, {'baidu_6.jpg': 0.726}, {'baidu_7.jpg': 0.798}, {'baidu_8.jpg': 0.82}, {'baidu_9.jpg': 0.529}, {'qihu_0.jpg': 0.654}, {'qihu_1.jpg': 0.565}, {'qihu_2.jpg': 0.523}, {'qihu_3.jpg': 0.851}, {'qihu_4.jpg': 0.887}, {'qihu_5.jpg': 0.721}, {'qihu_6.jpg': 0.771}, {'qihu_8.jpg': 0.931}, {'qihu_9.jpg': 0.764}, {'sogo_0.jpg': 0.615}, {'sogo_1.jpg': 0.797}, {'sogo_2.jpg': 0.699}, {'sogo_3.jpg': 0.69}, {'sogo_4.jpg': 0.895}, {'sogo_5.jpg': 0.746}, {'sogo_6.jpg': 0.743}, {'sogo_7.jpg': 0.691}, {'sogo_8.jpg': 0.891}, {'sogo_9.jpg': 0.929}]



def ssort(list):
    new_dict = {}
    for i in list:
        new_dict.update(i)
    return sorted(new_dict.items(), key=lambda x: x[1], reverse=True)


ssort(ll)