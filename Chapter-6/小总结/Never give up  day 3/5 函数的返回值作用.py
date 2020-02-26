#Author:never give up  range your dream

def txet01():
    print("逻辑函数01")


def txet02():
    print("逻辑函数01")
    return 0


def txet03():
    print("逻辑函数01")
    return 1,"哈哈",["a",1,2,"b"],{"haha":"xixi","aoo":"ee"}

x = txet01()
y = txet02()
z = txet03()
print(x)#返回值为None
print(y)#返回值为0
print(z)#返回值为一个元组 包含你定义的返回值 例如：(1, '哈哈', ['a', 1, 2, 'b'], {'haha': 'xixi', 'aoo': 'ee'})
        #可以看出返回值可以定义各种类型的数据 甚至可以包括返回函数等等。
        #函数返回值的作用是什么？函数返回值代表的是这段函数执行完毕后的结果。
        #因为后面的程序可能需要根据这个结果来进行下一步操作。