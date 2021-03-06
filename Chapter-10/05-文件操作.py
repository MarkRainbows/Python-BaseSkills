# author: Mark

"""
1.数据本地化
将数据以文件的形式，存储到本地磁盘中。
（程序中变量保存的数据都是存到内存中的，当程序运行结束内存中的数据会销毁）

常见的数据本地化方式：二进制文件(包含音频，视频，压缩包等), 普通文本文件, json和xml文件, 数据库文件等


2.文件操作(读和写)
文件操作的固定步骤：打开文件(新建文件) - 文件操作(读和写) - 关闭文件

3.打开文件
open(file, mode='r',...,encoding=None)  - 返回的是被打开的文件对象(文件句柄)

说明:
file - 字符串；需要打开的文件的路径(可以是绝对路径，也可以是相对路径)
    如果你取相对路径不是在主文件里，可能就会有相对路径问题："No such file or directory"  
    因为 python 的相对路径，相对的都是主文件。

    绝对路径: /Volumes/MKpossible/Python-BaseSkills/Chapter-10/files/蓝莲花.txt
    相对路径：(相对当前的py对应的目录)，需要把执行环境改为当前文件夹下，即可执行成功
            ./ -- 当前目录(./可以省略)   aaa.txt  ./aaa.txt
            ../ -- 当前目录的上层目录
            .../ -- 当前目录的上上层目录 
                

mode - 打开方式; 打开文件后不同的操作，对应的打开方式不一样
       'r'  -  默认值，以读的方式打开文件, 读出来的是字符串
       'w'  -  以写的方式打开文件
       'rb'/'br' - 以读的方式打开，读出来的数据是二进制
       'wb'/'bw' - 以写的方式打开，写二进制数据到文件中
       'a' - 以写的方式打开，追加
       '+' - 以读写方式打开
       
encoding - 文本文件编码方式,一般赋值为'utf-8'
           utf-8 - 支持中文编码
           gbk - 不支持中文编码
                
"""
# 以读的形式打开一个文本文件，保存到变量f中。对f进行操作，就是对被打开的文件进行操作
f = open('files/蓝莲花.txt', 'r', encoding='utf-8')

"""
4.文件的读操作
文件对象.read() - 从文件读写位置开始读到文件结尾(默认就是获取文件中所有的内容)
文件对象.readline() - 读一行内容
"""
# 读文件所有的内容
# content = f.read()
# print(content)

# 读一行
# content = f.readline()
# print('===:',content)

# 练习:将文件中的内容读完，要求一行一行的读
content = f.readline()
while content:
    print(content)
    content = f.readline()
f.close()

"""
5.文件的写操作
文件对象.write(字符串) - 将字符串中的内容写入到文件中（会完全覆盖原文件中的内容）

'w' - 完全覆盖,也可以用来创建新文件
'a' - 在原文件的最后添加
"""
f = open('/Volumes/MKpossible/Python-BaseSkills/Chapter-10/files/蓝莲花.txt', 'a', encoding='utf-8')
f.write('你好吗？')

"""
6.关闭文件
文件对象.close()  - 关闭指定的文件
"""
f.close()

