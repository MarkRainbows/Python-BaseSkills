#Author:never give up  range your dream
import time

def timer(func):  #当text1作为实参传进来时 嵌套函数就开始运行  于是就开始了下一个函数coco的运行
    def coco(*args,**kwargs):   #当运行完coco函数时返回的是coco的门牌号  于是就相当于 timer(text1)的运行结果为coco的门牌号
        start_time = time.time() # 函数即变量，所以 text = timer(text1)
        func(*args,**kwargs)                   # 最后text() 就相当于运行了coco 函数
        end_time = time.time()   # coco函数中给出了直接运行func()的参数
        print("the run time is%s"%(end_time-start_time))# 所以当运行text()时 就添加了装饰器 也不会改变原函数的调用方式
    return coco

@timer #text1 = timer(text1)
def text1():
    time.sleep(3)
    print("in the text1")

@timer
def text2(name,age):  #如果被调用的函数有参数怎么办呢？
    time.sleep(3)
    print("in the text2",name,age)  #只需要在被实际使用的参数中(coco)加入代表多个参数的形参即可

#text1 = timer(text1)# 这个操作可以用@timer 代替  当你想在哪个函数调用时就用@+装饰器的函数名
text1()
text2("旭东",24)#


