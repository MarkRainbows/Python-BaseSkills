# author： Mark

"""
1.堆和栈
内存区域中分堆区间和栈区间；栈区间的内存的开辟和释放是自动的，堆区间的内存是手动开辟手动释放的；
内存管理管理的是堆区间的内存。

2.数据的存储
a.python中所有的数据都是对象，都是保存在堆中的
b.python中所有的变量存储的都是存在堆中的数据的地址。存了对象的地址的变量又叫对象的引用 
c.默认情况下创建对象就会在堆中去开辟空间存储数据，并且将地址返回值;
  如果对象是数字，字符串会做缓存，而且使用的是会先去缓存中看之前有没有存过，
  如果有就直接返回之前的数据的地址，没有才开辟新的空间存储数据
  
3.数据的销毁
python中通过'垃圾回收机制'来管理内存的释放
原理：看一个对象是否销毁，就看这个的对象的引用计数是否为0。为0就销毁，不为0就不销毁
引用计数：对象的引用个数  

注意：垃圾回收其实就是回收引用计数是0的对象，但是系统不会时时刻刻的检测对象的引用计数是否是0。
     而是隔一段时间检测一次，如果检测到垃圾就回收


"""
from sys import getrefcount
"""
getrefcount(对象) - 获取指定对象的引用计数
"""

# 1.增加引用计数: 使用变量存对象的地址
list1 = [1]    # 对象[1]的引用计数是2
print(getrefcount(list1))
list2 = list1  # 对象[1]的引用计数是3
print(getrefcount(list1))
list3 = [list1, 100]  # 对象[1]的引用计数是4
print(getrefcount(list1))


# 2.减少引用计数
"""
a. 删除引用
b. 让当前对象的引用成为别的对象的引用
"""
print(id(list3[1]))
del list3[0]
print(getrefcount(list1))


list2 = 100
print(id(list2))
print(getrefcount(list1))

list3 = 100
print(id(list3))

print(getrefcount(100))
