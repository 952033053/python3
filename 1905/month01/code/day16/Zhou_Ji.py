'''
第一题：
1 单引号跟双引号的普通用法是相同的
2 单引号跟双引号的区别主要体现在当用单引号包起来的字符串里包含"的时候,
不需要使用转义符(\), 反过来也是一样
3 三引号有两种形式("""字符串内容""", 或者'''字符串内容''')
第二题：
代码一＝１　　　代码二＝[1]
第三题：
单星的，强制实参使用关键字传参
双星的，收集多余的关键字传参
第四题：
list01 = [1,2,3,4,5]
def map(list01):
    list02 = []
    list03 = []
    for i in list01:
        list02.append(i**2)
    yield list02
    for r in list02:
        if r > 10:
            list03.append(r)
    yield list03
for item in map(list01):
    print(item)
第五题:
第六题：
list01 = [{'name':'mocoy','age':18},{'name':'Adam','age':28}

      ,{'name':'Talor','age':26},{'name':'Charlie','age':15}]
for i in range(len(list01)):
    for r in range(i+1,len(list01)):
        if list01[i]['age'] > list01[r]['age']:
            list01[i], list01[r] = list01[r], list01[i]
print(list01)

'''
from shiyan import *
print(str_time01)