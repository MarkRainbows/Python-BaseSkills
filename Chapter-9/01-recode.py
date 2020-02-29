"""__author__ = 余婷"""
"""


1.函数的调用
过程：
回到函数声明的位置
用实参给形参赋值(传参)
执行函数体
获取返回值
回到函数调用的位置

压栈：
当调用函数的时候，系统会自动在栈区间开辟空间保存函数调用过程中产生的数据(形参,函数中声明的变量)

2.返回值
看有没有遇到return,遇到了函数的返回值就是return后面的值，没有返回值就是None。
函数调用表达式的结果就是函数的返回值


3.函数的参数
位置参数和关键字参数: 位置参数要在关键字参数的前面

参数的默认值: 参数名=值
不定长参数: *参数名; **参数名
参数类型说明: 参数名:类型名
对函数的返回值进行类型说明: def 函数名(参数列表) -> 返回值类型:

4.匿名函数
函数名 = lambda 参数列表:返回值
"""

def func1(a: int) -> int:
    return a**2

func1(10)
