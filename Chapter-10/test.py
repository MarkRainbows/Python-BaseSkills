# author: Mark

# def test1_func1():
#     def test1_func2():
#         print('我是模块1——1')
#     print('我是模块1')

# print('test1:', __name__)

# if __name__ == '__main__':
#     print('=======================')
#     print('test1')
#     test1_a = 100
#     for x in range(100):
#         print(x)

#     test1_func1()
#     print('=======================')





import requests

res = requests.get('https://wx4.sinaimg.cn/mw690/4674e705ly1fck5nxjt74j20yi1pc7mb.jpg')

with open('snow_river.jpg', 'wb') as f:
    f.write(res.content)

 












