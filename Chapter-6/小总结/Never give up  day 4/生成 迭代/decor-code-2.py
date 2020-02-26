import time



def colcker (func):  #装饰器  装饰函数使用  在不改变源代码及调用方式是 给原来函数添加新的功能

    def decor (*args,**kwargs):
        start_time = time.time()
        func(*args,**kwargs)
        end_time = time.time()
        print("the running time is %s"%(end_time-start_time))
    return decor

@colcker
def runtime ():
    time.sleep(2)
    print("texting running time")

@colcker
def text(name,age):
    time.sleep(2.5)
    print("the running time is ",name,age)
    



runtime()


# text("alex",32)





