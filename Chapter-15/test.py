import re

re_str = r'\d([A-Z]{2})'
result1 = re.fullmatch(re_str, '2HK')
print(result1)

result2 = re.match(re_str, '8KLsjdddd==ssdhfks')
print('-----')
print(result2)


print(result2.span())
print(result2.span(1))


print(result2.start(), result2.end())
print(result2.start(1), result2.end(1))

print(result2.group())
print(result2.group(1))

print(result2.string)


str1 = 'abc123hks362shjjk990kll'
result = re.search(r'\d{3}[a-z]{2}', str1)
print(result)


str1 = 'ab+c7hdjd8jss-sk9sjj78s9kk*k'
result = re.split(r'\d+|[+*-]+', str1)
print('=-=-=-=-')
print(result)



str1 = 'haja37jjkd89sdhs909nnna238==='
result = re.finditer(r'[a-zA-Z]{2,}(\d+)([a-z]+?)', str1)
print(result)
print(next(result))
print(next(result))
