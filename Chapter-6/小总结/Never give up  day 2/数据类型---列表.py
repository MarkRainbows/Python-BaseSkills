#Author:never give up  range your dream

import copy
code_name = ["stark","hulk","joker","Xu dong","cat","stark",["adad","gdsdfs"]]
fake_name = ["1 2 3 4 5 6"]

                       #列表的取值操作

# print(code_name[0:2])#顾头不顾尾，如果你想到哪个值结束 那么那个结束值的列表序号+1
# print(code_name[1:4])#顾头不顾尾，如果你想到哪个值结束 那么那个结束值的列表序号+1  （名为切片）
# print(code_name[-1])#取最后一个值
# print(code_name[-3:-1])#不管从最后开始往前取值，系统默认从左往右数列表，同样顾头不 顾尾
# print(code_name[-3:])#冒号后不写默认取到最后一个值
# print(code_name[:])#默认取全部的值
# print(code_name)
# print(code_name[0:-1:2]) #不连续切片 间隔一个取值 （感觉没啥用）


# code_name[0,1,2]注意列表不能同时取多个下标 要想取多个值只能用切片

                       #列表的增删改插

# code_name.append("OPPLE") #默认追加在列表的最后一个 增
# print(code_name)
# code_name.insert(1,"suolong")#新元素插入你想插入的列表下标位置，原先的列表元素默认往后移动 插
# print(code_name)
# code_name[2] = "supermilk"#想改动列表中某个元素，直接找到其列表下标并输入新的列表元素内容 改
# print(code_name)
# code_name.remove("suolong")#删除列表中你想要删除的元素，直接输内容  删
# print(code_name)
# del code_name[2] #删除列表中的元素，输入下标
# print(code_name)
# code_name.pop(2) #删除列表中的元素，输入下标
# print(code_name)

                       #列表的其他操作

# print(code_name.index("joker"))#查找列表元素中的索引，并给出元素在列表中的下标
# print(code_name.count("stark"))#统计元素在列表中的个数并返回值
# code_name.clear()#清空列表中的元素
# code_name.reverse()#反转列表 将列表中所有元素反转 最后一个排到第一个
# code_name.sort()#将列表排序 默认按照字母顺序排列，排序优先级 特殊字符>数字>大写字母>小写字母  字符串和整形的数字无法排序
# code_name.extend(fake_name) #合并列表，合并后的列表元素默认排在最后面
# print(code_name)

                                   #列表的复制
'''
list01 = ["abs","dust","adgsf","good",[1,2,3,4,[3,2,3]]] #按照首字母排序
list02 = ["ads","akl","kale"]


list02 = list01.copy()  #列表复制后  原列表更改元素 复制后列表不会跟着一起改
                        #但是涉及下一层的时候原列表更改元素 复制后的列表会一起更改
                        #因为原列表更改不再是一个表层  而是实际的数据
                        #如果想完全复制一份不更改的  import copy

import copy
list03 = copy.deepcopy(list01)

list01[2] = "milk code"
list01[-1][-1][1] = 66666

print(list01)
print(list02)
print(list03) 

'''


                              # 列表的竖向排列
# for l in code_name:
#     print(l) #让列表竖向排列






