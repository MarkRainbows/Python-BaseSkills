#Author:never give up  range your dream
import pickle
f = open("running","rb")

# x = json.loads(f.read()) #当你存入文件以全部为字符串格式时  如果想返回原来改动的数据类型并读取时 json.loads  "r"
x = pickle.loads(f.read())#pickle功能也相同 "rb"
#pickle.load(f.read())  效果等同上面
print(x["age"])


#json 支持不同语言之间的数据类型的转换，pickle只支持python本语言之间的数据类型转换但是支持范围是属于python所有数据类型