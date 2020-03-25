import time
from datetime import datetime, date, timedelta
res = time.localtime()
print(res)
time1 = time.strftime('%Y-%m-%d', res)
print(time1)

print(date.today())

time2 = datetime.now()
print(time2 + timedelta(hours=5))



