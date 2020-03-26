# author：Mark

import time, threading


"""
注意：当多个线程同时对同一个数据进行操作的时候，可能会出现数据混乱

多个线程对一个数据进行操作，一个线程将数据读出来，还没来得及存进去；
另一个线程又去读了，这个时候就可能产生数据安全隐患 - 解决问题的方案就是加锁

Thread - 线程类(创建子线程)
Lock - 锁(创建锁对象)
"""


class Account(object):
    def __init__(self, balance, name):
        self.balance = balance   # 余额
        self.name = name
        self.lock = threading.Lock()   # 创建锁对象

    def save(self, num):
        """存钱"""
        print('开始存钱')
        # 加锁
        self.lock.acquire()
        old_balance = self.balance
        time.sleep(5)
        self.balance = old_balance + num
        print('存钱成功！')
        # 解锁
        self.lock.release()

    def draw(self, num):
        """取钱"""
        # 加锁
        print('开始取钱!')
        self.lock.acquire()
        old_balance = self.balance
        time.sleep(4)
        self.balance = old_balance - num
        print('取钱成功!')
        # 解锁
        self.lock.release()


acount1 = Account(1000, '余婷')

# 支付宝存钱
t1 = threading.Thread(target=acount1.save, args=(1000,))
# 银行卡取钱
t2 = threading.Thread(target=acount1.draw, args=(500,))

t1.start()
t2.start()

t1.join()
t2.join()
print(acount1.balance)


