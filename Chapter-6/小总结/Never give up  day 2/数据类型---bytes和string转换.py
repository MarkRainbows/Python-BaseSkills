#Author:never give up  range your dream
# python 3 中 bytes类型 （二进制） 与 string （字符串）有着严格的区分  二进制数据不能再和字符串混用了 但可以相互转换。
a = "我爱你"
print(a)
print(a.encode("utf-8"))#字符串转换为二进制数据类型时 encode 编码  默认使用utf-8  可不写
print(a.encode().decode("utf-8"))#二进制转换为字符串时 decode 解码  默认使用utf-8  可不写
b = "I love you"
print(b.encode("utf-8"))
print(b.encode().decode())
# (记住是文件编码的转换  从二进制的文件编码到 utf-8的文件编码)


