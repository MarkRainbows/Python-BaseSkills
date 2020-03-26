# author：Mark

from threading import Thread, current_thread

"""
创建子线程，除了直接创建Thread的对象，还可以创建这个类的子类对象


注意：一个进程中有多个线程，进程会在所有的线程都结束才会结束;
     线程中的任务执行完了，线程就结束
"""


# 1.声明一个类继承Thread
class DownloadThread(Thread):
    # 想要给run方法传递数据，通过添加对象属性来传
    def __init__(self, file_name):
        super().__init__()
        self.file_name = file_name

    # 2.重写run方法
    def run(self):
        # 这个方法中的代码会在子线程中执行
        print('开始下载: %s' % self.file_name)


# 3.创建线程对象
t1 = DownloadThread('小黄人')
# 4.通过线程对象调用start在子线程中执行run方法
t1.start()
# t1.run()   # 直接调用run方法，会在主线程中执行
