#Author:never give up  range your dream
data = {
    '北京':{
        "昌平":{
            "沙河":["oldboy","test"],
            "天通苑":["链家地产","我爱我家"]
        },
        "朝阳":{
            "望京":["奔驰","陌陌"],
            "国贸":{"CICC","HP"},
            "东直门":{"Advent","飞信"},
        },
        "海淀":{},
    },
    '山东':{
        "德州":{},
        "青岛":{},
        "济南":{}
    },
    '广东':{
        "东莞":{},
        "常熟":{},
        "佛山":{},
    },
}
print(data.values())
# exit_flag = False
# while not exit_flag:
#     for l in data:
#         print(l)
#     usrchoose01 = input("请输入你的选择01 ：")
#     if usrchoose01 in data:
#         while not exit_flag:
#             for v in data[usrchoose01]:
#                 print("\t",v)
#             usrchoose02 = input("请输入你的选择02")
#             if usrchoose02 in data [usrchoose01]:
#                 while not exit_flag:
#                     for x in data[usrchoose01][usrchoose02]:
#                         print("\t\t",x)
#                     usrchoose03 = input("请输入你的选择03")
#                     if usrchoose03 in data [usrchoose01][usrchoose02]:
#                         for n in data[usrchoose01][usrchoose02][usrchoose03]:
#                             print("\t\t\t",n)
#                         usrchoose04 = input("已经为最后一级，请按b返回")
#                         if usrchoose04 == "b":
#                             pass
#                         elif usrchoose04 == "q":
#                             exit_flag = True
#                     if usrchoose03 == "b":
#                         break
#                     elif usrchoose03 == "q":
#                         exit_flag = True
#             if usrchoose02 == "b":
#                 break
#             elif usrchoose02 == "q":
#                 exit_flag = True











