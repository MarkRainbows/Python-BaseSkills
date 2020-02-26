#Author:never give up  range your dream

school = "kingbrige"#在程序中最前面的第一级声明的变量叫全局变量，各种函数中仍可以使用



def change_name(name):
    #global school 将局部变量声明为全局变量 不要使用
    school = "havel"#如果在函数里面声明了同全局相同的变量，那么优先使用函数的局部变量
    print("befor change",name,school)
    name = "Xudong"# name变量只在这个函数中起到作用，退出函数就无法使用，被称为局部变量
    print("after change",name,school)



name = "xudong"
change_name(name)
print(name)
print(school)

names = ["joker","solo","alex"] #全局变量
def change_name():
    names[0] = "iron-man"#局部变量   只有当全局变量为 列表 字典 集合的时候，函数才可以将局部变量改为全局变量。
    print(names)

change_name()
print(names)
