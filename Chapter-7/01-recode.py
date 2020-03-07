# author: Mark

"""
列表(list) - 有序、可变
[12, 34, 56]

列表元素的要求：任何类型的数据都可以作为列表元素

获取单个元素、获取部分元素(切片)、遍历

相关运算: +, *, ==/!=, in / not in, len(), list(), max(), min()
"""
name = '张三'
list1 = [12, 'abc', True, name, max('abcz')]
print(list1[-1])


# 补充： == 和 is
"""
== -  判断两个数据的值是否相等
is -  判断地址是否相等

python数据存储:1.给变量赋值的时候，如果数据的类型是数字或者字符串，不会直接开辟空间存数据，
              而是现在数字字符串对应的缓存区里面去查看是否已经存储过对应的数据。如果已经存了，
              直接将之前的数据对应的地址赋给变量。如果没有存储才会开辟空间存储数据。
              其他类型的数据，都是直接开辟空间存储数据。然后再把地址返回
              2.容器类型中的元素，在容器中不是直接存的值，而是元素值对应的地址
"""
list1 = [1, 2, 3]
list2 = [1, 2, 3]
list3 = list1
print(list1 == list2)
print(list1 is list2)
print('===:',list1[0] is list2[0])
print(list1 is list3)

number1 = 10
number2 = 10
print(number1 is number2)
