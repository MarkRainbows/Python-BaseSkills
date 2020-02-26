music = "sony read"
print(music.capitalize()) #将首字母大写
print(music.center(50,"*")) #将指定字符串居中  其余的用指定字符填充
print(music.count("s"))
sony = "abct\td"
print(sony.isalpha()) # 判断该字符是否全部为字母
print(range(2,-8))
print(sony.endswith("d")) # 判断该字符串是否是用指定的字符结尾
print(sony.startswith("ab")) # 判断该字符串是否用指定的字符开始
print(sony.expandtabs(tabsize=9)) # 在字符串\t 中添加指定的制表符
print(sony.find("x")) # 查找指定的字符是否在该字符串中 如果有返回下标 如果没有返回 -1
print(sony.index("a")) # 查找指定的字符是否在该字符串中 如果有返回下标 如果没有会报一个异常 ValueError: substring not found

read = " Ab Sony  Cnn  "

print(read.isalnum())# 当字符串中只要有一个字符是数字或者字母 就返回为Ture   当含有符号时就不管用"123...." ==  false
print(read.isalpha())# 当所有字符都是字母时返回Ture
print(read.isdigit())# 当字符串全部为数字才返回为Ture
print(read.isdecimal())# 必须也是全部为数字  而且数字必须是10进制
print(read.isnumeric())# 字符串中必须全部为数字字符 中文数字也可以
print(read.islower())#判断字符串是否为全部为小写
print(read.isupper())#判断字符串是否为全部为大写
print(read.isspace())# 判断字符串是否全部为空格
print(read.istitle())# 判断每个单词的开头是否为大写


cos = "AKL000000"
print(cos.join("***")) #  效果 *AKL*AKL*  join ("*"的符号至少要有两个,如果只有一个最后会打印 *)
print(len(cos))#返回 字符串的长度
print(max(cos))#返回字符串中字符编码值最大的那个
print(min(cos))#返回字符串中字符编码值最小的那个
print(cos.ljust(50,"-"))#字符左对齐
print(cos.rjust(50,"+"))#字符右对齐
print(cos.replace("K","king"))#替换字符
print(cos.rfind("i")) # 查找字符从右边开始  但是返回下标还是从左往右
print(cos.rindex("0")) # 查找字符从右边开始  但是下标不变还是从左往右
print(cos.rstrip()) #去掉最右边的空格和换行 和指定的字符
print(cos.lstrip()) #去掉最左边的空格和换行 和指定的字符
print(cos.strip()) #去掉两边的空格和换行  和指定的字符
print('agsk*shabkk*habba'.split('*')) #效果 ['agsk', 'shabkk', 'habba']
print('agsk\nshabkk\nhabba'.splitlines(keepends= False)) #效果 ['agsk', 'shabkk', 'habba']
print(cos.swapcase())#将字符串转换大小写
print(cos.zfill(50)) #效果  00000000000000000000000000000000000000000000AKL000
print(cos.title()) #将每个单词的开头字母变为大写













