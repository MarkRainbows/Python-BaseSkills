#Author:never give up  range your dream

# def foo():
#     print("in the foo")
#     def bar():# 这个bar函数相当于 foo 函数中的局部变量  所以只能在局部里面调用 不能再全局调用
#         print("in the bar")
#     bar()
# foo()


x = 0
def x1():
    x=1
    def x2():
        x=2
        def x3():
            x=3
            print(x) #局部作用域 和全局作用域的访问顺序   作用域只能从里往外找一层一层的找
            x3()     #最后的结果是 3
    x2()
x1()










