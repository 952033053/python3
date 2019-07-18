# l = []
# while True:
#     input01 = input('输入西游记你喜欢的角色:')
#     l.append(input01)
#     for i in l:
#         pass   min
#         # print(i)
#     if input01 == ' ':
#         # print(i)
#         break
# print(l)

# l = []
# while True:
#     input01 = input('输入成绩:')
#     if input01 == ' ':
#         break
#     l.append(input01)
# for i in l:
#     pass
# print(max(l))
# print(min(l))
# print(sum(l) / len(l))

# l = []
# l2 = []
# while True:
#     input01 = input('输入姓名:')
#     if input01 == ' ':
#         break
#     l.append(input01)
# for i in l:
#     if i not in l2:
#         l2.append(i)
#     else:
#         print(i + '名字已存在')
# for a in range(-1,-len(l2)-1,-1):
#     print(l2[a])
# l = []
# list01 = [54,25,36,59,78,36,46,12,33,11]
# for i in list01:
#     if i > 30:
#         l.append(i)
# print(l)
#
# l = []
# # a = 0
# # while a < 5:
# for i in range(1,6):
#     number = int(input('输入第%d数字:' %i))
#     l.append(number)
#     # a += 1
# print(max(l))
# max_value = 0
# for i in range(1,6):
#     number = int(input('输入第%d数字:' %i))
#     if max_value < number:
#         max_value = number
# print(max_value)


# list01 = [54, 25, 36, 59, 78, 36, 46, 12, 33, 11]
# max_value = list01[0]
# for i in range(1,len(list01)):
#     if max_value < list01[i]:
#         max_value = list01[i]
# print(max_value)
# 删除大于10的数字
# remove
# 删除元素:后一个替换前一个
# list01 = [9,25,12,8]
# for i in range(len(list01)-1,-1,-1):
#     if list01[i] > 10:
#         list01.remove(list01[i])
# print(list01)
# 列表换成字符串
# # '连接符'.join(列表)
# l = []
# while True:
#     input01 = input('输入字符串:')
#     if input01 == ' ':
#         break
#     l.append(input01)
# a = ''.join(l)
# print(a)


l = []
str01 = 'how-are-you'
list01 = str01.split('-')
list02 = ' '.join(list01[::-1])
print(list01)
