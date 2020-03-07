# author：Mark

import copy

list1 = [1, 2, 3, 4, 5, 6,[12,123,666]]
list2 = list1.copy()
list3 = copy.deepcopy(list1)
list1[-1][2] = 999

print(list1)
print(list2) 
print(list3) 
# 结果：
# [1, 2, 3, 4, 5, 6, [12, 123, 999]]
# [1, 2, 3, 4, 5, 6, [12, 123, 999]]
# [1, 2, 3, 4, 5, 6, [12, 123, 666]]

# 结论：
# 浅copy复制的是数字对应的地址，但是这些地址中对应的数据却没有变，所以如果在原列表中改变了数据对应的值，
# 那么浅copy列表中的值也会跟着该变。

# deepcopy 直接复制地址对应的数据，无论原列表怎么改变，deepcopy的列表都不会跟着改变。



