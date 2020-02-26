from collections import Iterable# 可用于 for循环的数据类型  都是可迭代对象  列表 字典 元组 字符串
print(isinstance([1,3,5],Iterable))
print(isinstance({},Iterable))
print(isinstance("abc",Iterable))
print(isinstance(set("asd"),Iterable))
print(isinstance((x for x in range (6)),Iterable))

print(isinstance(100,Iterable))



from collections import  Iterator# 可用于next()函数的都是迭代器    列表  字典  元组 本不是迭代器 可用 iter()变成迭代器

print(isinstance([],Iterator))
print(isinstance({},Iterator))
print(isinstance("abcde",Iterator))
a = iter([1,2,3,4])
print(isinstance(iter([]),Iterator))


