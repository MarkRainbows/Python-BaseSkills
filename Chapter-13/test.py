class Aniaml:
    def __init__(self, type, color, age=0):
        self.type = type
        self.color = color
        self.age = age


class Cat(Aniaml):
    def __init__(self, color, age=0, hobby=''):
        super().__init__('猫科', color, age)
        self.hobby = hobby


# an1 = Aniaml('犬科', '黄色')
# an2 = Aniaml('犬科', '黄色', 10)

# cat1 = Cat('白色')
# cat2 = Cat('灰色', 3)
cat3 = Cat('灰色', hobby='睡觉')
print(cat3.__dict__)
cat4 = Cat('灰色', 3, '睡觉') 
print()
print(cat4.__dict__)