#Author:never give up  range your dream
import sys
# print(sys.getdefaultencoding())  #
s = "你好"
print(s.encode("utf-8").decode("utf-8"))#程序默认文件编码是unicode  所以一开始没有 s.decode() 只有encode ()
print(s.encode("utf-8")) # S变量的编码默认是Unicode先编码为utf-8,以 byte类型的utf-8 例如 b'\xe4\xbd\xa0\xe5\xa5\xbd'
print(s.encode("GBK")) # S变量的编码默认是Unicode先编码为GBK,以 byte类型的 GBK 例如  b'\xc4\xe3\xba\xc3''
print(s.encode("GBK").decode("GBK"))

                        #如果要从GBK转换成utf-8
# s_gbk = s.encode("gbk")
# print(s_gbk)
# sx = s_gbk.decode("gbk").encode("utf-8") #先将s_gbk 转换为GBK格式，然后将s_gbk解码为Unicode 再将Unicode编码为utf-8格式
# print(sx)
#
# s_gb2312 = s.encode("gb2312")
# print(s_gb2312)    #先将s_gb2312 转换为gb2312格式，然后将s_gb2312解码为Unicode 再将Unicode编码为gbk格式
# sv = s_gb2312.decode("gb2312").encode("gbk")
# print(sv)
