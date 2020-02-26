#Author:never give up  range your dream


list_1 = set([1,3,5,7,6,6,9,10])
list_2 = set([2,4,6,8,10,3])
list_3 = set ([1,3,5])
list_4 = set([66,88,99])
print(list_1)
# list_1 = set (list_1)     #set 将一个普通列表变为一个集合，集合自带元素不重复，元素无序的特性。
# print(list_1,type(list_1))
# print(list_2,type(list_2))
# print(list_1,type(list_1))


# print(list_1.intersection(list_2)) #两个集合取交集 (list_1 & list_2)
# print(list_1.union(list_2)) #两个集合取并集 (list_1|list_2)
# print(list_1.difference(list_2)) #取 list_1 有的而 list_2 没有的 (list_1-list_2)
# print(list_1.symmetric_difference(list_2)) #除开list_1和list_2的交集去剩下的值 (list_1 ^ list_2)
# print(list_1.isdisjoint(list_4)) # 如果两个集没有交集   返回为Ture
# list_1.update([66,77,88])#在集合中添加多项元素
# list_1.add(34)#只能在集合中添加一个元素 '''
# print(list_1)



# list_1.remove(3) #指定从集合中删除一个元素
# print(list_1)
# print(list_1.pop())#随机从集合中删除一个元素并返回删除的值
# # list_1.clear()#清空整个集合
# print(list_1.copy())#浅复制一份
# list_1.discard(10) #如果指定的删除元素在集合里面 就删除一个指定的元素 如果没有 不报错 不返回任何值
# print(list_1)




# print(list_3.issubset(list_1)) #如果list_3是list_1的子集 就返回为Ture
# print(list_3 <= list_1) #与上楼效果相同
# print(list_1.issuperset(list_3)) #如果list_1是list_3的父集 就返回为Ture
# print(list_1>=list_3)#与上楼效果相同
# print(len(list_1)) #测试集合的长度
# print(1 in (list_1)) #测试元素是否在集合中
# print(1  not in (list_1)) #测试元素是否在集合中

