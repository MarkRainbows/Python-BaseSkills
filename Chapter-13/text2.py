
class Time:
    def __init__(self):
        self._second= 0

    @property
    def second(self):
        return self._second

    # '01:11 - 71'
    @second.setter
    def second(self, value: str):
        times = value.split(':')
        self._second = int(times[0])*60 + int(times[1])


times = []
while True:
    value = input('时间:')
    if value == 'end':
        break
    # 创建对象，并且将输入的内容赋给时间
    t = Time()
    t.second = value
    times.append(t)

print(times)
