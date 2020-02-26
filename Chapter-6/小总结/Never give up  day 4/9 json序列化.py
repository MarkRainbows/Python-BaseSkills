#Author:never give up  range your dream
import json
import pickle
info = {"name":"xudong","age":24}

f = open("running","wb")

#f.write(json.dumps(info)) #当你把一个字典存入文件里面时，里面的数字不是字符串类型 所以无法存进去字符串格式  "w"
 #这时需要将这个字典的所有数据,全部转化为字符串  只限制简单的数据类型 "wb"
f.write(pickle.dumps(info))
#pickle.dumps(info,f)  效果等同上面
f.close()

#json 支持不同语言之间的数据类型的转换，pickle只支持python本语言之间的数据类型转换但是支持范围是属于python所有数据类型

#原则上只用一次dunmp或者load
