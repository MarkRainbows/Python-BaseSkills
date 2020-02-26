#Author:never give up  range your dream
import time

                                     # 高阶函数定义
# 1  把函数名当做实参传给宁外一个函数 (在不修改被修饰函数的源代码情况下为其添加其他功能)
# 2  函数的返回值包含了函数名       （满足二者中的一个即为高阶函数）

def bar():
    print("in the bar")

def text (func):#此时为 text(bar)
    print(func)# print(bar)  如果光是打印bar函数名的话就会打印出 bar 函数在内存中的地址(也就是bar函数的门牌号)
    func()# bar()    这个相当于调用bar()  所以给出返回值 in the bar

text(bar)  # 把bar函数名当做实参传给text 函数

x = 1
y = x

func = bar  # 函数即变量   那么变量可以去赋值其他变量 y = x   那么函数也可以去赋值给其他函数 func = bar
func()


def coco():
    time.sleep(3)
    print("coco")



def xixi(func):
    start_time = time .time()
    func()
    end_time = time.time()
    print("func run time is %s"%(end_time-start_time))

xixi(coco) #没有改变被修饰函数的源代码 但是被修饰函数的调用方式被改变了(当如果要使用装饰器时 被修饰函数调用方式就改变了) 。
           # （被修饰函数的调用方式coco()）


def bar():
    print("in the bar")

def text2(func):
    print("加了功能")
    return func

bar = text2(bar)# 这个门牌号又是一个函数 而这个函数的功能就是给门牌号进行修饰附加其他功能。
bar()# 所以所bar()运行时会先找到这个门牌号 但是这个门牌号又是一个函数会给这个门牌号先附加其他功能，等添加完功能后再找
     #被修饰函数门牌号对应的实体函数  （也就相当于没有改变被修饰函数的调用方式）
