# author: Mark

import requests

"""
python中去做http请求，需要使用一个第三方库: requests
"""
"""
get(url, 参数字典) - 返回响应
"""
# 1.向服务器发送get请求
# a.手动拼接url
# url = 'https://www.apiopen.top/satinApi?type=1&page=1'
# response = requests.get(url)
# print(response)

# b.自动拼接url
url = 'https://www.baidu.com/'
response = requests.get(url, {'type': 1, 'page': 1})
print(response)#返回响应的状态码

# 2.获取响应头
header = response.headers
print(header)

# 3.获取响应体
"""
a.获取二进制格式的响应体
"""
content = response.content
print(type(content))

"""
b.获取json格式响应体 - 自动将json数据转换成python
"""
json = response.json()
print(type(json))

"""
c.获取字符串格式的响应体
"""
text = response.text
print(type(text))


# 应用：下载网络图片
url = 'https://timgsa.baidu.com/timg?image&quality=80&size=b10000_10000&sec=1543395098&di=2a5bbaa5600097b050ba69a688672de9&src=http://p0.qhimgs4.com/t0112e7ebfdef7f923d.jpg'
response = requests.get(url)
image_data = response.content
with open('王也.jpg', 'wb') as f:
    f.write(image_data)
