#Author:never give up  range your dream


                                        # 装饰器的定义

#装饰器本质是个函数，用来装饰其他函数， 原话就是为其他函数添加附加功能
# 装饰器的原则    1 不能修改被装饰函数的源代码  2 不能修改被装饰函数的函数调用方式 3 装饰器相对于被装饰的函数是透明的
                  # 相当于被装饰的函数感觉不到装饰器的存在


#要实现装饰器的知识储备
#1 函数即为“变量
#2 高阶函数
#2 嵌套函数
# 高阶函数 + 嵌套函数 --> 装饰器

#函数即为变量
# python的内存回收机制  当变量赋值的内容再也没有变量名时 则会被python内存机制给抹除。 函数回收机制也跟变量一样



# 匿名函数  有的函数可以不定义函数名 直接使用 例如
doc = lambda x:x*3
doc(3)#这就是匿名函数  lambda x:x*3 就相当于函数体 如果跟函数体没有定义函数名或者变量名 那么它就会被回收
print(doc(3))#所以必须得跟这个lambda赋值一个变量




#函数即为变量的例子

# def func()
#     print("in the func")# 属于错误的函数  因为没有bar的实际函数体  所以一旦调用bar()就无法找到  属于错误
#     bar()*******
#
# func()



def bar():
    print("in the bar")#  函数即为变量  bar函数名就相当于变量名 而里面的print（"in the bar"）为函数体就相当于变量的赋值
                       #  x = 1  --->   bar = print("in the bar")
def func():
    print("in the func")
    bar()

func()  #这段函数正确 因为都同时定义了 bar 和 func的函数体  所以调用的时候能够找到   正确


def foo():
    print("in the foo")
    suo()

def suo():
    print("in the suo")

foo()  #这段函数也是正确 唯一跟上面的区别就是 suo函数位置在foo的下面 这不影响 因为在 foo()函数执行之前
       # 两个函数 suo foo 就已经定义了函数体 ，所以再次调用的时候跟先后无关



# def foo():
#     print("in the foo")
#     suo()
# foo()  # 这段函数就为错误  因为suo 函数是在已经调用了 foo()这段函数之后才定义的，所以foo函数无法找到suo函数   错误
#
# def suo():
#     print("in the suo")




