# 5.循环输入大于0的数字进行累加，直到输入的数字为0，就结束循环，并最后输出累加的结果。
'''
sum = 0
while True:
    num = int(input("请输入一个数字："))
    sum = sum + num
    if num == 0 :
        print("stop")
        break
    print(sum)
'''



# 6.求s=a+aa+aaa+aaaa+aa...a的值，其中a是一个数字。例如2+22+222+2222+22222(此时共有5个数相加)，
# 几个数相加由键盘控制。 1.程序分析：关键是计算出每一项的值。


# basis = int(input("请输入一个基本的数"))
# n = int(input('请输入这个数字的位数 '))
# arr = [0] * n  # 定义一个长度为n，初值全部为0的一维数组。
# b = basis  # 通项
# sum = 0
# for i in range(n):# 6
#     arr[i] = basis
#     sum += basis
#     basis = basis * 10 + b
# print("%d=" % sum, end='')
# for i in range(n):
#     print("%d" % arr[i], end='')
#     if i < n - 1:
#         print("+", end='')



# 7.输入三个整数x,y,z，请把这三个数由小到大输出。
'''
num01 = int(input("输入第一个数"))
num02 = int(input("输入第二个数"))
num03 = int(input("输入第三个数"))

if num01 < num02:
    x = num01
    num01 = num02
    num02 = x

elif num01 < num03:
    y = num01
    num01 = num03
    num03 = y
    
elif num02 < num03:
    z = num02
    num02 = num03
    num03 = z
print(num03,num02,num01)


'''

# a.根据n的值的不同，输出相应的形状
# n = 5时             n = 4
# *****               ****
# ****                ***
# ***                 **
# **                  *
# *
'''
num = int(input("请输入一个数："))
for i in range(-num,0):
    print("*"*abs(i))
'''


# b.根据n的值的不同，输出相应的形状(n为奇数)
# n = 5               n = 7
#   *                    *
#  ***                  ***
# *****                *****
#                     *******

'''

num = int(input("请输入一个数："))
for i in range(1,num+1):
    if i % 2 == 0:
        continue
    else:
        print(("*"* i).center(num))
'''

# 九九乘法表
'''
for i in range(1,10):
    j = 1
    for j in range(1,i+1):
        print("%d x %d"%(j,i),"=",j*i)

'''

# 10.这是经典的"百马百担"问题，有一百匹马，驮一百担货，大马驮3担，中马驮2担，两只小马驮1担，问有大，中，小马各几匹？
'''
for x in range(1,101):
    for y in range(1,101):
        for z in range (1,101):
            if x + y + z == 100 and 3 * x + 2 * y + 0.5 * z == 100:
                print(x,y,z)

'''

# 11.
# 我国古代数学家张邱建在《算经》中出了一道“百钱买百鸡”的问题，题意是这样的：
# 5 文钱可以买一只公鸡，
# 3 文钱可以买一只母鸡，
# 1 文钱可以买3只雏鸡。现在用100文钱买100只鸡，那么各有公鸡、母鸡、雏鸡多少只？请编写程序实现。
'''
for x in range(1,101):
    for y in range(1,101):
        for z in range (1,101):
            if x + y + z == 100 and 5 * x + 3 * y + (1/3) * z == 100:
                print(x,y,z)
'''

# 12.小明单位发了100元的购物卡，小明到超市买三类洗化用品，洗发水（15元），香皂（2元），牙刷（5元）。
# 要把100元整好花掉，可如有哪些购买结合？
'''
count = 0
for x in range(1,101):
    for y in range(1,101):
        for z in range(1,101):
            if 15 * x + 2 * y + 5 * z == 100:
                print(x,y,z)
                count += 1
print(count)

'''

# 4. 有⼀一分数序列列：2/1,3/2,5/3,8/5,13/8,21/13...求出这个数列列的第20个分数
# 分⼦子：上⼀一个分数的分⼦子加分⺟母 分⺟母: 上⼀一个分数的分⼦子 fz = 2 fm = 1 fz+fm / fz

# 2/1  3/2  5/3

# fz = 2
# fm = 1
# for i in range(1,21):
#     if i == 1:
#         res = fz / fm
#         print("2 / 1")
#         continue
#     fz , fm = fm + fz , fz
#     # fz = fm + fz
#     # fm = fz - fm
#     print("%d / %d" % (fz, fm))








































































































