# author： Mark

from threading import Thread
import time,datetime,random
"""
线程对象.join() - 等待线程对象中的任务执行完成
"""


class Download(Thread):
    def __init__(self, film_name):
        super().__init__()
        self.film_name = film_name

    def run(self):
        print('开始下载:%s' % self.film_name)
        a = random.randint(5, 12)
        time.sleep(a)
        print('%s开始结束' % self.film_name, '耗时%d秒' % a)


if __name__ == '__main__':
    t1 = Download('小黄人')
    t2 = Download('地心游记')
    time1 = time.time()
    t1.start()
    t2.start()

    # t1和t2中的任务都执行完成后才执行后面的代码
    t1.join()
    t2.join()

    time2 = time.time()
    print('总共时间:', time2 - time1)
