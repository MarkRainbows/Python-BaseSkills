#Author:never give up  range your dream

# 位置参数的调用  关键字参数的调用
def text(x,y):
    print(x)
    print(y)

text(1,2)# x y 为形式参数 没有具体的内存  1 2 为实际参数有具体的内存 (位置参数调用 实参和形参必须一一对应)
text(y=2,x=1)# 关键字参数调用 无需一一对应  只要赋予每个形参对应的值

def text02(l,j,k):
    print(l)
    print(j)
    print(k)
text02(1,2,3)
text02(1,k=3,j=2)#如果参数调用中既含有位置参数和关键字参数，规则是关键字参数必须在位置参数的后面
text02(1,2,k=3)#实参必须和前面的形参一一对应后，关键字参数才能定义剩余的形参。


# 默认参数调用

def text(x,y=2): #默认参数的特点：给形参默认定义某个实参，当定义实参时如果没有定义到这个形参 那么这个形参将以默认实参的方式
                 #传值给形参，如果重新定义这个默认的形参 ，那么这个实参将会覆盖默认的形参。
    print(x)
    print(y)
text(1)
text(1,3)       #用途：给一些程序默认安装的时候传值等等


# 参数组

def text(x,*args):#*args 可以接受多个不固定的实参，并将这些实参以元组的方式打印.
    print(x)
    print(args)
text("ad",1,2,3,4,5,6,7,) #把多个位置参数转化元组

def text(**kwargs):#**kwargs 把多个关键字参数转化为字典
    print(kwargs)
    print(kwargs["name"])#取字典中单个的值
    print(kwargs["age"])#取字典中单个的值
    print(kwargs["love"])#取字典中单个的值
text(name="xu dong",age = 24,love = "露") #关键字参数

def text(name,age=24,*args,**kwargs):#一个形参可以包含 默认参数 参数组 等等
    print(name)
    print(age)
    print(args)
    print(kwargs)
text("xudong",age=32,love = "露",car = "Tesla")#实参要与形参一一对应 格式也要相对应
