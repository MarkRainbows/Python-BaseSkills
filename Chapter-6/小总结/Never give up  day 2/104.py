#Author:never give up    just do it

list01 = set ([1,3,6,6,6,8,9])
list02 = set ([2,3,4,5,6,6,89,9])
list03 = set ([1,3,6])

print(list03.issubset(list01))
print(list01.issuperset(list03))
print(len(list01))
print(1 in list02)
print(1 not in list02)



# print(list01,type(list01))
# list02.pop()
# list02.discard(89)
# print(list02)

# print(list01.intersection(list02))
# print(list01.union(list02))
# print(list01.difference(list02))
# print(list01.symmetric_difference(list02))
# print(list01.isdisjoint(list02))
# list01.update([44,231,2342])
# list01.add(55)
