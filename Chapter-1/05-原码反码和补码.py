# author: Mark


"""
1.计算机数据的存储
计算机能够直接存储的是数字，并且存的数字的补码


2.计算机内存大小单位
位(bit)
1字节 = 8位
1KB = 1024字节
1MB = 1024KB
1GB = 1024MB
1TB = 1024GB



3.原码：符号位+真值 （用最高位表示符号位，后面的其他位表示数字的二进制）
     符号位： 0 -> 正, 1 -> 负数
     真值 ：数字对应的二进制值
10(原码) = 00001010  
-10(原码) = 10001010

4.反码：
正数的反码和原码一样。负数的反码是符号位不变，其他位上的数取反(0变成1，1变成0)
10(反码) = 00001010
-10(反码) = 11110101

5.补码： 
正数的补码和原码一样。负数的补码就是反码加1
10(补码) = 00001010
-10(补码) = 11110110

注意：数据存储和运算的时候采用的是补码。看结果看的是原码
"""

"""
如果计算机存储的是原码：
3：0011
2：0010
3+2 = 0101 = 5

原码：
3-2 = 3+(-2) = 1101 = -5
3: 0011
-2:1010

补码：
3(补) = 0011
-2(补) = 1101(反) = 1110(补)
0011(补)+1110(补) = 0001(补) = 0001(原) = 1

2-3
2：0010（原）= 0010（补）
-3：1011（原） = 1100（反）= 1101（补码）
0010（补）+ 1101（补码） = 1111（补码）= 1110（补码-1，反） = 1001(原码)= -1

总结 :
正数原码，反码，补码都一样
负数原码最高位为1，反码最高位不变其他全部反转，补码就是负数的反码加1
进行补码运算，结果看的是补码的原码 

"""
