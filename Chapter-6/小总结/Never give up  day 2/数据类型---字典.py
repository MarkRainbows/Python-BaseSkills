#Author:never give up  range your dream


#字典具有无序性 通过关键词 key 取出对应的值
info = {'num01':'娜美',"num02":"罗宾","num03":"山治","num04":"索隆","num05":"弗兰奇","num06":"路飞"}




                                  #关于字典的增删改查


print(info["num01"])
info ["num01"] = "雷利"#如果有相同的key 就会给key替换最新的值，如果没有相同key 就会添加一组key-value(增和改)
#del info["num01"] #删除字典的key及相对应的值
# info.pop("num01") #删除字典的key及相对应的值
# info.popitem()#随机删除一组数据 (有可能删除最后一组)
print(info.get("num08"))#查找字典对应的key，如果有打出相应的值，如果没有显示none
print("num06" in info)#判断key值是否存在字典里 如果有显示True 没有 False'''


                             #关于字典的多级目录操作
Gunlist = {"handgun":["p-77","patt-55","dust-66"],
         "shutgun":["s868","s906","r006"],
         "mchinegun":["scale","m416","m16"],
         "sinpergun":["kar_98","awm","m24"]
         } #二层字典
ss = {"num01":"dfasa","34":"5464"}


Gunlist["shutgun"][0] = "xxx" #更改多级目录中的内容
print(Gunlist.values())#只打印valnue
print(Gunlist.keys())#只打印key
Gunlist.setdefault("handgak",{"robat"})  #更改字典中的一组数据 如果有相同key则字典中的原key_value值不变，
                                        # 如果没有则会新添加一组数据
print(Gunlist)
info.update(ss)#将 ss字典中的数据更新到info 中 如果有相同的key则会更新value，没有相同就会添加进去
print(info)
print(info.items())#将原字典变为列表模式 里面的key-value值变为元组形式。
c = dict.fromkeys([6,8,9],"ATM")#效果 {8: 'ATM', 9: 'ATM', 6: 'ATM'} 前面对应为key 后面对应为valnue 更改其中一组的valnue
print(c)                                                             #其他的也会相应更改
print(Gunlist)

                                   #循环字典
for l in info:
    print(l,info[l])#打印对应的key值，打印对应的value值。








