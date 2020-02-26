#Author:never give up  range your dream
import time

def log():   # 当你的程序需要重复使用一段代码时 你可以把这段代码写成一个函数 在需要这段代码时直接调用函数名就行。
    time_log = "%Y-%M-%D %X"             #调用函数 有 1方便代码重复使用 2 函数功能可扩展性 3保持代码一致性
    time_current = time.strftime(time_log)
    with open("日志", "a+")as f:
        f.write("% send with time\n"%(time_current))

def text01():
    print("红牛正能量01")

    log()
def text02():
    print("红牛正能量02")

    log()
def text03():
    print("红牛正能量03")

    log()

text01()
text02()
text03()