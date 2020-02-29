# 0.写一个匿名函数，判断指定的年是否是闰年
'''
r_year = lambda year:"改年是闰年"if year % 4 == 0 and year % 100 != 0 or year % 400 == 0 else "该年不是闰年"

print(r_year(2018))
print(r_year(2014))
print(r_year(2000))

'''


# 1.写一个函数将一个指定的列表中的元素逆序( 如[1, 2, 3] -> [3, 2, 1])(注意:不要使用表自带的逆序函数)
'''
def list01(x:list):
    list02 = x[::-1]
    return list02


print(list01([1,2,3,4]))

'''
# 3.写一个函数，统计指定列表中指定元素的个数(不用列表自带的count方法)
'''
def list02(n:list):
    count = 0
    for i in n:
        count += 1
    print(count)


list02([1,2,3,4,5,6])

'''

# 4.写一个函数，获取指定列表中指定元素的下标(如果指定元素有多个，将每个元素的下标都返回)
# 例如: 列表是：[1, 3, 4, 1] ,元素是1, 返回:0,3
'''
def index1 (n:list,m:int):
    for index01 in range(len(n)):
        if m == n[index01]:
            print(index01)

index1([1,2,3,4,5,2],2)

'''
# 5.写一个函数，能够将一个字典中的键值对添加到另外一个字典中(不使用字典自带的update方法)

'''
def dict01 (x:dict,y:dict):
    list110 = list(tuple(x.items()))
    list111 = list(tuple(y.items()))
    list110.extend(list111)
    print(dict(list110))


dict01({"abc":1},{"bcd":2})

'''

# 6.写一个函数，能够将指定字符串中的所有的小写字母转换成大写字母；所有的大写字母转换成小写字母(不能使用字符串相关方法)

'''
def str01(s:str):
    for i in s:
        if i<="Z" and  i >= "A":
            print(chr(ord(i)+32),end="") #将循环的字符横向打印
        elif i <= "z" and i >= "a":
            print(chr(ord(i)-32),end="")

str01("iglol")

'''

# 7.写一个函数，能够将指定字符串中的指定子串替换成指定的其他字符串(不能使用字符串的replace方法)
# 例如: func1('abcdaxyz', 'a', '\') - 返回: '\bcd\xyz'
'''
def str02 (x:str,m:str,n:str):
    for i in x:
        if i == m:
            i = n
            print(i,end="")
        else:
            print(i,end="")


str02('abcdcc456fgfghf56','c','+')

'''


# 8.实现一个输入自己的items方法，可以将自定的字典转换成列表。列表中的元素是小的列表，里面是key和value (不能使用字典的items方法)
# 例如:{'a':1, 'b':2} 转换成 [['a', 1], ['b', 2]]

'''
def items01(x:dict):
    list02 = []
    for items in x:
        list03 = []
        list03.append(items)
        list03.append(x[items])
        list02.append(list03)
    print(list02)


items01({"a":1,"b":2,"c":3})
'''












