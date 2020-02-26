#Author:never give up  range your dream

def bar():
    print("in the bar")

def text2(func):
    print("加了功能")
    return func

bar = text2(bar)# 这个门牌号又是一个函数 而这个函数的功能就是给门牌号进行修饰附加其他功能。
bar()# 所以所bar()运行时会先找到这个门牌号 但是这个门牌号又是一个函数会给这个门牌号先附加其他功能，等添加完功能后再找
     #被修饰函数门牌号对应的实体函数
