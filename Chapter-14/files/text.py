class Student:
    def __init__(self, name, age, score):
        self.name = name
        self.age = age
        self.score = score

    def __add__(self, other):
        return self.score + other.score



s1 = Student('a1', 23, 566)

s2 = Student('a2', 42, 588)

print(s1 + s2)



