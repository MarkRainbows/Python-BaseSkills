x = 0
def grandpa (): #内置函数 一层一层的往里面走
    x = 1
    def dad ():
        x = 2
        def son ():
            x = 3
            print(x)
        son()
    dad()
grandpa()
import time

def deco ():
    time.sleep(3)
    print("in the text 1")
    return deco

print(deco)

