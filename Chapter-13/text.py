'''
class Person:
    num = 99

    def __init__(self, name):
        self.name = name

    def eat(self, food):
        print('%s在吃什么%s' % (self.name, food))

    @classmethod
    def destroy(cls):
        print(Person.num)
        print(cls.__name__)
        p2 = cls('阿花')
        p2.eat('木瓜')


    @staticmethod
    def hit():
        print('殴打小动物')
        print(Person.num)


p1 = Person('小强')
p1.eat('食物')
Person.destroy()
Person.hit()


# 练习：
# 数学类，属性：pi  功能：求两个数的和,  求一个圆的面积

import math


class Math:
    p1 = math.pi

    @staticmethod
    def sum1(num1, num2):
        return num1 + num2

    @classmethod
    def area(cls, r):
        return cls.p1 * r**2


print(Math.sum1(10, 20))
print(Math.area(5))


class XDMath(Math):
    pass


print(XDMath.sum1(10, 50))
print(XDMath.area(6))
'''

'''
class Person:

    __num = 20

    def __init__(self):
        self.name = '花花'
        self.__age = 36

    def user(self):
        print(self.name)
        print(self.__age)
        print(Person.__num)

    def show(self):
        self.user()

p1 = Person()
p1.user()
# p1.__age   #不可调用
# Person.__num


'''


class Person:
    def __init__(self, name='小红'):
        self.name = name
        self._age = 60

    @property
    def age(self):
        if 0 < self._age < 1:
            return '婴儿'
        elif self._age < 18:
            return '未成年'
        elif self._age < 70:
            return '成年'
        else:
            return '老年'

    @age.setter
    def age(self, value):
        if not isinstance(value, int):
            print('输入的不是数字')
            raise ValueError
        elif not 0 < value < 100:
            print('输入的年龄不在范围内')
            raise ValueError
        self._age = value

p1 = Person()
print(p1.age)
p1.age = 90
print(p1.age)





# 练习：声明一个时间类，有一个属性是以秒的形式保存时间
# 不断的输入时间，以'XX:XX'的形式输入。输入多少个时间就保存多少个时间对象。知道输入end为止

'''
class Time:
    def __init__(self):
        self._sec = 0

    @property
    def sec(self):
        return self._sec

    @sec.setter
    def sec(self, value:str):
        time = value.split(':')
        self._sec = int(time[0])*60 + int(time[1])

    def __repr__(self):
        return 'shijian' + str(self.sec)


value = input('时间')
t1 = Time()
t1.sec = value
print(t1.sec)


'''


# 类的继承


'''
class Person:

    num = 99

    def __init__(self):
        self.name = '张三'
        self.age = 10
        self.sex = 'nan'

    def eat(self):
        print('%s在吃饭' % self.name)

p1 = Person()


class Student(Person):
    pass

s1 = Student()
s1.eat()
print(Student.num)
print(s1.name)
print(s1.age)
print(s1.sex)
s1.name = '阿花'
print(s1.name)
print(p1.name)


'''

'''
class Person:

    def __init__(self):
        self.name = '张三'
        self.age = 18
        self.sex = 'male'

    def show(self):
        print('%s在吃饭' % self.name)

    def func1(self):
        print('你好')

    @staticmethod
    def sta():
        print('我是人类')

p1 = Person()
p1.sta()

class Student(Person):


    def new(self):
        print('子类新方法')

    @classmethod
    def mesage(cls):
        super().sta()


    @staticmethod
    def sta():
        # super().sta()  #静态方法不能使用super（）
        print('我是新人类')

    def show(self):
        super().show()
        print('我是学生')
        super().func1()
        s1 = Student()
        
        
        
# s1.new()
# Student.mesage()
# Student.sta()
# s1.show()
s1.show()

'''

'''
class Person:
    num = 60

    def __init__(self, name):
        self.name = name
        self.age = 0


class Student(Person):
    num1 = 80

    def __init__(self, name):
        super().__init__(name)
        self.study = '001'


s1 = Student('张三')

print(Student.num ,Student.num1)
print(s1.name, s1.age, s1.study)

'''

# 练习：
# 声明一个动物类，有属性：年龄，颜色，类型。
#  要求创建动物对象的时候类型和颜色必须赋值，年龄可以赋值也可以不赋值
# 声明一个猫类，有属性:年龄，颜色，类型, 爱好
# 要求创建猫对象的时候，颜色必须赋值，年龄和爱好可以赋值也可以不赋值，类型不能赋值


class Animal:
    def __init__(self,type,color,age = 0):
        self.type = type
        self.color = color
        self.age = age




class Cat(Animal):
    def __init__(self, color, age = 0,hobby = ''):
        super().__init__('猫科',color,age)
        self.type = '猫科'
        self.color = color
        self.age = age
        self.hobby = hobby
a1 = Animal('犬科','黄色')
a2 = Animal('犬科','灰色',3)






