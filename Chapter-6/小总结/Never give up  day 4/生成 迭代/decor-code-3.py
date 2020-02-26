
name,age = "Alex", "32"

def check(func):
    def authorize (*args,**kwargs):
        name01 = input("your name:")
        age01 = input("your age:")
        if name01==name and age01==age:
            print("Authorized entry !")
            res = func(*args,**kwargs)
            print("---------->")
            print(res)
        else:
            print("wrong !")
    return authorize


@check
def info ():
    print("infomation :",name,age)
    return "from home"

info()
