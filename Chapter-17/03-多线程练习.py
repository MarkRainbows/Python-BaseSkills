# author：Mark

import requests
from threading import Thread


def download(url: str):
    """下载函数"""
    image_data = requests.get(url).content
    file_name = url.split('/')[-1]
    with open('images/'+file_name, 'wb') as f:
        f.write(image_data)


# 1.下载接口对应的数据
url = 'https://www.apiopen.top/satinApi?type=1&page=1'
data_dict = requests.get(url).json()
datas = data_dict['data']
for dict1 in datas:
    # 拿到一个图片地址，就为它创建一个线程对象，用来在子线程中下载这张图片
    t = Thread(target=download, args=(dict1['profile_image'],))
    t.start()

print('下载完成')


# 使用正则获取数据
import re
url = 'https://www.apiopen.top/satinApi?type=1&page=1'
text = requests.get(url).text

all_profile_image = re.findall(r'"profile_image":"(.+?)",', text)
for image_url in all_profile_image:
    Thread(target=download, args=(image_url,)).start()
