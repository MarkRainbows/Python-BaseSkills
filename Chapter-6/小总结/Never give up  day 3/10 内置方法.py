#Author:never give up  range your dream

# python 一开始启动就会自带的内置方法。来了解一下内置方法有哪些。
''''''
a = abs(-20) # abs()取数字的绝对值
print(a)

print(all([0,1,-6]))# all() 如果可迭代对象里面的元素都为真的话那么就返回为Ture 否则为False
print(any([0,1,-6]))# any() 如果可迭代对象里面的元素其中任意一个为真的话那么就返回为Ture 没有任何元素为False
print(bin(255)) #把整数十进制转二进制
# bool()判断真假 0-False  其他--Ture  空列表和空子典都为---False
b = bytearray("abcd",encoding="utf-8")#默认字符串不能更改其内容 但是bytearray可以将字符串变为列表 以二进制形式更改
b[1]=50#没什么用
print(b)
# callable()#判断是否可以调用 函数和类可以
# chr(98)#必须输出数字标号 然后对应ASCLL吗的字符
# ord("a")#反过来输入ASCLL字符对应的数字编号

# exec(a)  #a 是一段注释代码  这个方法可以将这个 a 注释代码直接执行
# c = {}
# dir(c) 打开c的内置方法
#enumerate(a) 将a列表的每个元素加上下标
#eval("asd")把字符串变为字典
#filter()#通过lambda表达式来过滤数据  匿名函数lambda
res = filter(lambda n:n>5,range(10))
a = frozenset([1,2,3,44,5,6])#将集合变为不可更改的属性
print(globals())#将当前文件所有的变量和对应的值以一个字典的形式打印出来
locals()#打印局部的变量
hash("xudong")#文件内部算法将特定的字符全部一一映射相应的数字，方便查找
#oct()#转换为八进制
#hex()转换为十六进制
v = {1:2,3:2,2:5}
#sorted(v.items()，key= lambda x:x[1])#将字典按key排序成为一个新的列表,或者value排序
#zip 让两组相同类型的数据一一对应 如果另一组产生多的则不会对应





