# author：Mark


"""
一个进程默认有一个线程，这个线程叫主线程。默认情况下，所有的代码都是在主线程中执行的
"""

import time, datetime


def download(film_name):
    print('开始下载:%s' % film_name, datetime.datetime.now())
    time.sleep(3)   # 程序执行到这个地方，线程会阻塞3秒(停3秒)，再执行后面的代码
    print('%s下载结束' % film_name, datetime.datetime.now())




# if __name__ == '__main__':
download('小黄人')
download('地心游记')

