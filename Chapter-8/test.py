
def get_operation(char):
    # char = '+'
    if char == '+':
        # 求和的功能
        def sum(*args, **kwargs):
            # args = (10,20,30)
            """求多个数的和"""
            sum1 = 0
            for item1 in args:
                sum1 += item1
            for key in kwargs:
                sum1 += kwargs[key]
            print('yt')
            return sum1  # = sum()

        return sum
re = get_operation('+')
# re(10, 20, 30) - 调用函数获取返回值
print(re(10, 20, 30))  # 60  = 10+20+30




