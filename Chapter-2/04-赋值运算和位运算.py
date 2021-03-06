# author : Mark

# 1.赋值运算符：=，+=， -=， *=， /=，  %=，  //=， **=
"""
所有赋值符的左边必须是变量; 组合的赋值运算符的左边的变量必须已经赋值；
所有赋值运算符最终的会进行赋值操作
"""
# 2. = - 直接将右边的结果赋给左边的变量
num = 100

# 3. +=， -=， *=， /=，  %=，  //=， **=
"""
变量 += 值 --> 相当于 变量 = 变量 + 值
变量 -= 值 --> 相当于 变量 = 变量 - 值
变量 *= 值 --> 相当于 变量 = 变量 * 值
...
"""
num1 = 1
num1 += 10   # num1 = num1+10 = 1+10
print(num1)

num1 *= 2    # num1 = num1*2 = 11*2
print(num1)

num1 %= 2    # num1 = num1 % 2 = 22%2
print(num1)

# 3.运算符的优先级
"""
数学运算符 > 比较运算符 > 逻辑运算符 > 赋值运算符
优先级高的先算。如果有括号，先算括号里面的

数学运算符中: ** > *, /, %, // > +, -


"""
num = 10 + 20 > 25 and True < 2
# num = 30 > 25 and True < 2
# num = True and True
# num = True
print(num)

num = 10 + (20 > 25 and True < 2)
# num = 10 + (False and True < 2)
# num = 10 + False
# num = 10
print(num)

num = 10 + 2 * 3 ** 2
print(num)

# 4.位运算：&(按位与)，|(按位或)，^(按位异或), ~（按位取反），<<(左移), >>(右移)
# 位运算是针对二进制中每一位进行的相关操作

"""
a. 数字1 & 数字2  -> 二进制的每一位进行与运算，运算的时候如果都为1结果就是1，否则就是0
1 & 1 - 1
1 & 0 - 0
0 & 1 - 0
0 & 0 - 0

与的特点：一位上的数如果和1与，就会保留这一位上的数。如果和0与，就会将这一位置0
11010 & 00111 = 00010

与运算的应用：判断一个数的奇偶性(最优解答)
            将数字和1与，如果结果是0，就说明这个数是偶数；如果结果是1，说明这个数是奇数
"""
"""
3(原/补) = 0011
2(原/补) = 0010
3 & 2 = 0011 & 0010 = 0010(补)


-2 = 1010(原) = 1101(反) = 1110(补)
3 & -2 = 0011 & 1110 = 0010(补)  # 
"""
# ！！！！ （位运算 ===>补码来计算===>结果看原码）
print(3 & 2)
print(3 & -2)

print(5 & 1, 111 & 1, 123 & 1)   # 1 1 1
print(100 & 1, 12 & 1, 67238 & 1)  # 0 0 0

"""
b.数字1 | 数字2 - 如果有一位是1结果就是1，两个都为0结果才是0
1 | 1 - 1
1 | 0 - 1
0 | 1 - 1
0 | 0 - 0

1101 | 1010  - 1111

3 | 20 
000011 | 010100 = 010111(补)

-3 | 20
111101(补) | 010100 = 111101(补)  
"""
print(3 | 20)
print(-3 | 20)

"""
c.按位取反
~ 数字 - 将每一位取反(0变成1，1变成0)
~1 = 0
~0 = 1

~2
010 -> 101(按位取返后的补码) = 110(在取补码的反码) = 111(原码) 
"""

print(~2)

"""
d.按位异或
数字1 ^ 数字2  - 每一位如果相同就为0，不同为1
1 ^ 1 - 0
1 ^ 0 - 1
0 ^ 1 - 1
0 ^ 0 - 0

11 ^ 2
01011 ^ 00010 = 01001(补) (整数的补码就是原码)

"""
#  11^ -2  取得是两个的补码进行运算  运算后看最高位是否有1  有1 为负   再将这个运算后的补码进行取原码计算
print(11 ^ 2)

num = 10
print(num ^ 10)

"""
e.左移
数字1 << n(位数) - 左移指定的位数就是在二进制的后面加指定个数个0
                  相当于：数字1 * (2**n)
10 << 1
01010 << 1 = 010100 = 20
01010 << 2 = 0101000 = 2^5 + 2^3 = 32 + 8 = 40

-10 << 1
11010 -> 10110(补码) << 1 = 101100(补)= 101011(反)=110100 = -20
"""
print(10 << 1)
print(10 << 2)
print(-10 << 1)

"""
f.右移
数字1 >> n(位数)  右移指定的位数就是在二进制的后面删除指定个数个0
                 相当于: 数字1 // (2**n)
20
010100 >> 2 = 0101 = 5
0101 >> 1 = 010 = 2
010 >> 1 = 01 = 1
01 >> 1 = 0 = 0
"""
print(-20 >> 2)

