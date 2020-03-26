import time
from datetime import datetime, date, timedelta

# res = time.localtime()
# print(res)
# time1 = time.strftime('%Y-%m-%d', res)
# print(time1)

# print(date.today())

# time2 = datetime.now()
# print(time2 + timedelta(hours=5))


res = time.localtime()
print('%s-%s-%s' % (res.tm_year, res.tm_mon, res.tm_mday))

text1 = time.strftime('%Y %m %d', time.localtime())
print(text1)

# time_obj = time.strptime('2019/11/30', '%Y/%m/%d')
# print('-=-=-=-=')
# print(time_obj)
# print('-=-=-=-=-=')


print(date.today())
time1 = datetime.now()
print(time1.year, time1.month, time1.day)
print(time1+timedelta(days=1))
print(time1+timedelta(hours=10))

a = datetime.strptime('2018-12-31 23:59:10', '%Y-%m-%d %H:%M:%S')
print(a)
print(a + timedelta(seconds=50))