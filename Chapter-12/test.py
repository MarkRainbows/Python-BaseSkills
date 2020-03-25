class Student:
    # Student类的对象只能有name,study_id,age和sex属性
    # __slots__ = ('name', 'study_id', 'age', 'sex')

    def __init__(self, name, age):
        self.name = name
        self.study_id = '001'
        self.age = age
        # self.sex = ''


stu1 = Student('夏明', 18)
stu1.neme = '小明'
stu1.sex = '男'



class Person:
    # 声明了一个字段number
    number = 61

    def show_number(self):
        print('人类的数量：%d' % Person.number)


print(Person.number)
Person().show_number()


class_name = Person.__name__
print(class_name, type(class_name))



print(stu1.__dict__)