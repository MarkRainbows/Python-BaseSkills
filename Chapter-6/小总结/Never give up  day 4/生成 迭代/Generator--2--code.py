def customer(name):
    print("%s 准备好吃海鲜啦"%(name))
    while True:
        seafood = yield
        print("海鲜 %s 准备好啦 ，海鲜被 %s 吃啦" % (seafood, name))


customer("Alex")


import time

def producter(name):

    a = customer("A")
    b = customer("B")
    a.__next__()
    b.__next__()
    print("准备开始做海鲜啦")
    for i in range(6):
        time.sleep(1)
        print("做了两份海鲜")
        a.send(i)
        b.send(i)

producter("xudong")




