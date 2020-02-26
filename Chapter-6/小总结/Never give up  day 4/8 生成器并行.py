#Author:never give up  range your dream
import time

def custoumer (name):
    print("%s准备吃包子了"%(name))
    while True:
        baozi = yield
        print("包子[%s]来啦，包子被[%s]吃啦"%(baozi,name))


def producter (name):
    a = custoumer("redbull")
    b = custoumer("cocobull")
    a.__next__()
    b.__next__()
    print("开始做包子啦")
    for i in range(5):
        time.sleep(2)
        print("做了两个包子")
        a.send(i)
        b.send(i)

producter("旭东")






