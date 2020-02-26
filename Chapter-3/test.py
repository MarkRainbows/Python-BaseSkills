
'''
# a = 'abcde'
# print(a[-1:0:-1])
# print(a[0:10:2])
# str1 = 'abc123abc'
# print(str1[-1:3])  # '' - 空串
# print(str1[3:-1])

# str1 = 'abc123abc'
# print(str1[:4:1])
# print(str1[:4:-1])
# print(str1[4::-1])

# str1 = 'abc'
# str2 = '123'
# print(str1 + str2, str1, str2)
# print(('*'*10+'%'*10)*3)
print('abc' == 'abc')
print('abc' != 'abc')
print('abc' == 'cba')

print('1' < 'a')

'''

read = '12334一二'
print(read.isdecimal())

cos = "AKLo\n"
print(cos.join("***"))
print(cos.ljust(50," "))#字符左对齐
print(cos.rjust(50," "))#字符右对齐
# print(cos.replace("K","king"))#替换字符
print(cos.rfind("K"))
print(cos.rstrip('Lo'))
