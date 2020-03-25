import threading
import time,datetime


def func1(names):

    print('%s start print'%(names),datetime.datetime.now())
    time.sleep(3)
    print('%s end print'%(names),datetime.datetime.now())
    print('%s下载完成'%(names),threading.current_thread()) #打印当前子线程



if __name__ == '__main__':


    t1 = threading.Thread(target=func1,args=('mad_max',))  # args 后面接元组形式
    t2 = threading.Thread(target=func1,args=('fast&furios',))  # args 后面接元组形式


    t1.start()
    t2.start()
