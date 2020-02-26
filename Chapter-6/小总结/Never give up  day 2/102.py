#Author:never give up    just do it

coffee = {101:"baby",102:"dear",103:"love",104:"lover"}
coffee[105] = "my dear"
for l in coffee:
    print(l,coffee[l])
# # del coffee [101]
# # coffee.pop(102)
# coffee.popitem()
# print(coffee.get(106))
# print(106 in coffee)
print(coffee.items())
print(coffee.get(101))
print(coffee[101])


gunlist = {"handgun":["p-77","patt-55","dust-66"],
         "shutgun":["s868","s906","r006"],
         "mchinegun":["scale","m416","m16"],
         "sinpergun":["kar_98","awm","m24"]
         } #二层字典
ss = {"num01":"dfasa","34":"5464",103:"xxxxx"}

# coffee.update(ss)
# print(coffee)



del gunlist["shutgun"][2]
print(gunlist["shutgun"])
# gunlist["shutgun"][1] = "xxx"
# gunlist.setdefault("real gun",["xxxxx","yyyyy"])
# print(gunlist)
# print(gunlist["shutgun"])
# print(gunlist.values())
# print(gunlist.keys())
