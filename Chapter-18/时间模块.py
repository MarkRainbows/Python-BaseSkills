
#  1. time模块

# time模块中主要提供了很多和时间相关的函数，和一个类：struct_time
# 时间戳  --  指定时间到1970年1月1日0时0分0秒的时间差，单位是秒
# a 使用时间戳的场景  1 节约时间存储成本   2 对时间进行加密
import time

# 1.获取当前时间(单位：秒) 以时间戳的形式返回

# res = time.time()


# 2.本地时间   localtime() --  获取当前本地时间

# res = time.localtime()
# print('%s-%s-%s' % (res.tm_year, res.tm_mon, res.tm_mday))


# 格式时间
# time.strftime(时间格式，时间对象)----- 将时间对象转换成指定格式的时间字符串
# 时间格式 --  字符串，字符串中带有相应的时间格式，用来获取指定的时间值
# %Y - 年  %m - 月   %d - 日

# 时间对象  -  time.strftime()

text1 = time.strftime('%Y%m%d', time.localtime())
print(text1)

#  time.strptime(字符串，时间格式) - 返回时间对象（将时间字符串中的时间提取出来）

time_obj = time.strptime('2019/11/30', '%Y/%m/%d')
print('-=-=-=-=')
print(time_obj)
print('-=-=-=-=-=')

from datetime import datetime , time ,date,timedelta

# datetime 模块中主要包含三个类：
# date(日期) -- 只能对年月日对应的时间进行表示和操作
# time（时间）-- 只能对时分秒对应的时间进行操作和表示
# datetime（日期和时间） - 既能对年月日又能对时分秒进行操作和表示

print(date.today())


time1 = datetime.now()
print(time1.year, time1.month, time1.day)

# date 和 datetime对象支持时间的加减操作
# 时间对象+timedelta对象
# 时间对象-timedelta对象


print(time1 + timedelta(days=1)) #能加天数
print(time1 + timedelta(hours=10))

# 将字符串转换成datetime对象
a = datetime.strptime('2018-12-31 23:59:10', '%Y-%m-%d %H:%M:%S')
print(a + timedelta(seconds=50))









