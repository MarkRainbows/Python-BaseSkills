"""__author__ = 余婷"""

"""
1.什么是字符串（str）
字符串是python中一种常用的有序但是不可变的容器类的数据类型，可以同时存储多个字符。属于序列

字面量：使用单引号或者双引号将任意字符括起来，就是字符串常量
'hjh是否就是23as+-'， "是89===——238jsNM是"

字符：指的就是字符串中的每一个单元。注意，python中只有字符的概念没有字符类型

"""
num = 10

"""
2.字符串中的内容
a.普通字符：包含数字字符、字母、普通符号：+，-（），%#@等、中文、韩文、日语等
'123'， 'hsja', '*&sd23顺'

b.转义字符：通过反斜杠将一些字符转换成有特殊功能或者特殊意义的字符
\n - 换行
\t - 制表符
\' - 表示一个单引号
\" - 表示一个双引号
\\ - 表示一个\

注意：一个转义字符代表一个字符

c.阻止转义: 在字符串的最前面加r/R,可以阻止转义字符转义

"""
print('\tabc\n123')
print('abc\'123')
print("ab\"c'123")
print('abc\\n123')

print(r'abc\n12\\3')
print(r'\b')

print(r"abc\n12\\3")
a = "艾克"

print(a.encode("utf-8"))
print(a.encode("GBK").decode("GBK"))
# print(2**7)   只能针对 128位
# unicode(2**16)   65536个字符进行编码
# print(chr(编码值))   将字符编码转换成字符
# ord(字符)  获取字符对应的编码值
print(chr(97))  #char(97)== a
print(chr(0x4e00))  #中文范围  4e00 - 9FA5

print(ord("刘"),ord("旭"),ord("东"))




idc = "\u4e1c"
print(idc) #可直接加\u 四位16进制编码值

name = "abcd"
print(name[-1:-5:-1])

print(len(name))
print(name[3])
print(name[-1:-2:-1])

print("abc"+"bcd")
print("abc"*3)
print("*"*10 + "%"*10)

print("2" > "-a")
#中文范围  4e00 - 9FA5



# print("是否是中文:", 0x4e00 < = ord(字符) < = 0x9fa5)

# print("是否是中文:","\u4e00" <= 字符 <= "\u9FA5")

print(bool(''))  #空字符串转化为bool False  ，其余全部转化为Ture

a = "abc".capitalize()
print(a)


import random

num001 = random.randint(10, 20)
print(num001)
newnum01 = "python18080" + str(num001).rjust(3, "0")
print(newnum01)
