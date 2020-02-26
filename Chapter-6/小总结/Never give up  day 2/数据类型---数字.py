#Author:never give up  range your dream
# 1  数据类型初识
# （数字） 在python中 整形数字 int 不管整形数字大小是否超过2**64  python都将自动转化成整形
# 2  浮点型  可以认识成为包括小数点的数字  可以认知为小数
# 3  复数型 包含实数和虚数  例如x+yj  （一般不会用到它）
# 4  布尔值 True 代表1  False 代表 0 只有两个值
a,b,c = 1,3,5
d=a if a>b else c #三元运算，变量取值的内容取决于满足某个条件
e=a if a<b else c #三元运算，变量取值的内容取决于满足某个条件
print(d)
print(e)


a,b,c = 1,3,5

d = a if a > b else c
e = a if a < b else c





