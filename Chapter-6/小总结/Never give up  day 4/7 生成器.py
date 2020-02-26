#Author:never give up  range your dream

#列表生成式
a = [i*2 for i in range(10)] #在一个列表中写一个表达式则称之为列表生成式
print(a)

c = (i*2 for i in range(10))# 将列表生成式的 [] 改为 () 则变为生成器 generator。(只有调用的时候才生成元素)
# generator 只是生成了一个表达式 并没有将列表中的元素打印在内存中 所以当列表内元素过多时可以使用generator
print(c.__next__())
print(c.__next__())   #生成器只能一个一个的往后面取值，不能朝前面返回，而且永远只存在一个值在内存中
print(c.__next__())   #这种next方法很笨拙 基本不会使用 ,但是可以将随时跳出生成器 进行其他操作
print(c.__next__())

                            #如果将函数的取值变为生成器那就非常容易

#列如使用斐波那契数列函数 (1,1,2,3,5,8,13)

def fib(max):
    n,a,b= 0,1,1
    while n < max:
        yield b   # yield 此时就是将一个函数变为了生成器 generator
        # print(b)
        a, b = b, a + b
        n = n + 1
    return "done" #程序异常的时候返回的结果。


x = fib(10)
for i in x:
    print(i)