#Author:never give up  range your dream

                                      #文件读写模式

f = open("歌词")
data = f.read()# 打开"歌词"文件 文件句柄 打开后可以对文件进行 读写等其他操作。
f = open("歌词","r",encoding="utf-8") # "r" 以只读方式的打开文件 不可写
print(f.read())
f = open("歌词02","w",encoding="utf-8")# 以只写的方式打开文件  不可读
print(f.write("oaaoaaoeeaoea"))# "w" 以重新创建文件的方式 写在文件里 如果源文件有内容 用write模式将会覆盖源文件内容
f = open("歌词","a",encoding="utf-8")
print(f.write("\noooaaaaoaaaaaeaolalalaea"))# "a"模式 给源文件追加新的内容 不会覆盖源文件  不可读

f = open("歌词","r",encoding="utf-8")
for line in range(10):
    print(f.readline().strip())  # 如果要进行多行数据打印
print(f.readline())# readline 表示打印一行数据


# 如果要进行全部数据打印  则需要将文件进行循环
''' 将文件一行一行载入内存中 读一行 删一行  并且读到第10行打印分隔符
f = open("歌词","r",encoding="utf-8")
count = 0
for line in f:
   if count == 3:
       print("-------------分隔符----------------")
       count += 1
       continue
   print(line)
   count+=1'''''

# f = open("歌词","r",encoding="utf-8")
# print(f.read(10))#指定打印字符多少
# print(f.tell())#定位字符串光标的位置
# print(f.seek(0))#将光标字符位置回到初始位置  也可以自定义回到任意位置seek(10)回到10的位置

'''f = open("歌词","a",encoding="utf-8")
f.write("\nasdadadagagdsfaf")
f.flush()#将内存中的文件信息刷新到硬盘上
import sys,time
for l in range(20):
    sys.stdout.write("*")
    sys.stdout.flush()
    time.sleep(0.3)'''

# f = open("歌词","a",encoding="utf-8")
# print(f.truncate(10))#指定从0开始截断到10的位置的内容覆盖文件  无论光标跳到哪儿 截断永远是从0开始.

#f = open("歌词","r+",encoding="utf-8") #文件句柄读写  当前文件读写 （追加到最后） （1 经常用到  其他不多用）
#f = open("歌词","w+",encoding="utf-8") #文件句柄写读  新建文件写读   (追加到最后)
#f = open("歌词","a+",encoding="utf-8") #文件句柄追加读  当前文件追加  (追加到最后)
#f = open("歌词","rb") #文件句柄  二进制读文件
# f = open("歌词02","wb")#文件句柄  二进制写文件
# f.write("adfsfafaaf\n".encode()) #将hello world 转化为二进制文件
# f.close()

'''f = open("歌词","r",encoding="utf-8")
f_new = open("歌词02","w",encoding="utf8")

for line in f:
    print(line)
    if "Stranger to blue water" in line:
        line = line.replace("Stranger to blue water","Stranger to red water")
    f_new.write(line)
f.close()
f_new.close()'''  #以重新创建文件的方式修改文件内容

with open("歌词","r",encoding="utf-8") as f:#with 语句的作用是 打开文件后不用操作关闭 close .
    for line in f:
        print(line)