#Author:never give up  range your dream



code_name = ("opple")
'''
print(code_name.count("o")) #统计字符串"o"的个数
print(code_name.capitalize())#让第一个字母大写
print(code_name.center(50,"-"))#让字符居中 不够的自定填充符号 效果----------------my name is code v-----------------
print(code_name.encode())#让字符串变为二进制  b'opple'
print(code_name.endswith("e"))#字符串是什么结尾 如果一样为 Ture
print(code_name.expandtabs(tabsize=50)) #效果my     （中间默认空格填充50个字符代替\t）   name is code v
'''


# code_name = ("opple {name}")
# print(code_name.format(name = "solo"))# 替换字符内容 填充效果
# code_name = ("op{x}ple{z}")
# print(code_name.format_map({'x':'code','z':'v'}))#同format效果一样 只不过会用到字典
# print(code_name.find("e"))# 查找指定字符并返回字符索引下标
# print(code_name.index("e"))#查找指定字符并返回字符索引下标

'''
print(code_name.isdigit())#判断字符串是否全部为数字
print(code_name.istitle())#判断首字母是否为大写 只有Opple 才返回为真
print(code_name.isdecimal())#是否为十进制数字 必须字符串内全部为数字时才返回为真
print(code_name.isalnum())#查看字符是否为阿拉伯数字 当只包含英文字母和数字时 才返回为真
print(code_name.isidentifier())#判断是否为合法字符 （以变量命名规则为准）
print(code_name.isupper())#判断字符串是否全部为大写
print(code_name.islower())#判断字符串是否全部为小写
print(code_name.isnumeric())#判断字符串是否全部为数字 
print(code_name.isprintable())#判断是否可以打印 一般字符串都能打印 所以为真
print(code_name.isspace())#判断是否全部为空格，只有当全部为空格时才返回为真 
'''




# code = ('STARK')
# print(code_name.join("sssS")) # 在字符串前后加s  效果如同 sopplesopples
# print(code.ljust(50,'*'))#效果 my name is code v********************************* 总共为50个字符
# print(code.rjust(50,'*'))#效果 *********************************my name is code v 总共为50个字符
# print('ADGAFAG'.lower())#全部转换为小写
# print('aafasf'.upper())#全部转换为大写
# print("\nsfafafaf\n".strip())#去掉两边的空格与换行   \n为换行命令符   \t为空格命令符
# p = str.maketrans("abcdefj",'1234567')
# print("code v".translate(p))#按数字顺序加密   字符串简单加密
# print("code v".replace('v','V'))#指定替换字符
# print("code v".rfind('v'))#将指定的字符替换为对应的字符索引下标
# print("1+2+3+4".split("+"))#把分隔符取消掉 效果['1', '2', '3', '4']
# print("Code v".swapcase())#将字符大小写反转 cODE V
# print("Code v".zfill(50))# 不够的用0补位 用在16进制补位上面  00000000000000000000000000000000000000000000Code v '''
#



