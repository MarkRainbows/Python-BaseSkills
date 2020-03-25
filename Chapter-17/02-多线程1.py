"""__author__ = 余婷"""
import threading
import time, datetime

"""
python中提供了threading模块，来支持多线程技术

默认创建的线程叫主线程，其他的线程叫子线程。如果希望代码在子线程中执行，必须手动创建线程对象
"""


def download(film_name):
    print('开始下载:%s' % film_name, datetime.datetime.now())
    time.sleep(5)   # 程序执行到这个地方，线程会阻塞5秒(停5秒)，再执行后面的代码
    print('%s下载结束' % film_name, datetime.datetime.now())
    print('下载%s:' %film_name, threading.current_thread())


if __name__ == '__main__':
    # download('小黄人')

    # 1.创建线程对象
    """
    a.
    Thread - 线程类
    b.
    Thread(target=函数名,args=参数列表) - 直接创建线程对象, 返回线程对象
    函数名 = 需要在当前创建的子线程中执行的函数变量
    参数列表 = 元祖，元祖的元素就是调用函数的时候给函数传递的参数
    """
    t1 = threading.Thread(target=download, args=('小黄人',)) #创建子线程
    t2 = threading.Thread(target=download, args=('地心游记',))

    # 2.在子线程中执行任务
    """
    在这儿就是调用t1对应的线程中调用download函数，并且传递一个参数'小黄人'
    """
    t1.start() #让子线程开始运行
    t2.start()
