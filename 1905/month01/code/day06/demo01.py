# list01 = []
# list02 = []
# list03 = []
# list04 = []
# for i in range(1,11):
#     list01.append(i**2)
# for i in list01:
#     if i % 2 == 0 and i > 5:
#         list04.append(i + 1)
#     if i % 2 == 0:
#         list02.append(i)
#     else:
#         list03.append(i)

# list01 = [i**2 for i in range(1,11)]
# list02 = [i for i in list01 if i % 2 == 0]
# list03 = [i for i in list01 if i % 2 == 1]
# list04 = [i+1 for i in list02 if i > 5]
# print(list01)
# print(list02)
# print(list03)
# print(list04)

# month = int(input(':'))
# if month < 1 or month > 12:
#     print('输入有误')
# elif month == 2:
#     print('28')
# elif month in (4, 6, 9,11):
#     print('30')
# else:
#     print('31')
#方法一:
# tuple01 = (31,28,31,30,31,30,31,31,30,31,30,31)
#
# total_day = 0
# for i in range(month - 1):
#     total_day += tuple01[i]
# total_day += day
# print(('是这年的第%d天' %total_day))
# #方法二:
# month = int(input('请输入月份:'))
# day = int(input('请输入日期:'))
# total_day =sum(tuple01[:month-1])
# total_day += day
# print(('是这年的第%d天' %total_day))
l = []
dict01 = {'许':5,'念':8}
dict0 = {'sa ':6,'念asd ':9}
l.append(dict01)
l.append(dict0)
print(l[0])
