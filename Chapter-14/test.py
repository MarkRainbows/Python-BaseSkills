from sys import getrefcount
"""
getrefcount(对象) - 获取指定对象的引用计数
"""

# 1.增加引用计数: 使用变量存对象的地址
list1 = [1]    # 对象[1]的引用计数是2
print(getrefcount(list1))
list2 = list1  # 对象[1]的引用计数是3
print(getrefcount(list1))
list3 = [list1, 100]  # 对象[1]的引用计数是4
print(getrefcount(list1))



print(id(list3[1]))
del list3[0]
print(getrefcount(list1))


list2 = 100
print(id(list2))
print(getrefcount(list1))

list3 = 100
print(id(list3))

print(getrefcount(list1))