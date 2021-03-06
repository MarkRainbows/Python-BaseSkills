# author: Mark


"""
1.什么是字典（dict）
字典是python中内置的容器类的数据类型,可变，无序的。字典的元素是键值对

2.字典的表现形式：使用大括号括起来，大括号中是键值对，多个键值对之间用逗号隔开
键值对- 键:值
键(key) - 不可变的；唯一的  (一般使用字符串作为key)
值(value) - 任何类型的数据
"""

dict1 = {'aa': 100, 10: 'abc', (10, 20): 'hello'}

# 列表和字典不能作为key
# dict2 = {{'a': 1}: 100, 10: 'abc', (10, 20): 'hello'}  # TypeError

# key是唯一的
dict2 = {'aa': 100, 'aa': 200, 'bb': 300}
print(dict2)   # {'aa': 200, 'bb': 300}


"""
什么时候使用字典: 
如果一个容器里面存储的数据是不同意义的数据(数据之间需要区分),就使用字典
"""
# 用一个变量来存储一个学生的信息：姓名、年龄、电话、成绩、学号
student = ['小明', 28, '1627399992', 30, '1982001', 98]
print(student[0])

student = {'name': '小明', 'age': 28, 'tel': '1627399992', 'score': 30, '学号':'1982001'}
print(student['name'])