# def int01(numbre):
#     '''
#     计算整数的个十百千的位数和
#     :param numbre:
#     :return:
#     '''
#     result = numbre%10
#     result += numbre // 10%10
#     result += numbre //100 %10
#     result += numbre //1000
#     return result
# numbre = int(input('请输入四位整数:'))
# print(int01(numbre))

# def input01(weight_liang):
#     jin = weight_liang // 16
#     liang = weight_liang % 16
#     return str(jin)+'斤零' + str(liang) + '两'
# weight_liang = int(input('请输入四位整数:'))
# print(input01(weight_liang))

# def score01(score):
#     '''
#
#     :param score:
#     :return:
#     '''
#     if score > 100 or score < 0:
#         return '输入有误'
#     if 90 <= score:
#         return  '优秀'
#     if 80 <= score:
#         return  '良好'
#     if 60 <= score:
#         return  '及格'
#     else:
#         return  '不及格'
#
# print(score01(90))
# def score01(list01):
#     for r in range(0,len(list01)-1):
#         for c in range(r+1,len(list01)):
#             if list01[r] == list01[c]:
#                 return True
#     return False
# list01 = [3,81,5]
# print(score01(list01))

def is_leap_year(year):
    #     if year % 4 == 0 and year % 100 != 0 or year % 400 == 0:
    #         return True
    #     else:
    #         return False
    return year % 4 == 0 and year % 100 != 0 or year % 400 == 0


# def get_day_by_month(year, month):
#     if month < 1 or month > 12:
#         return 0
#     if month == 2:
#         if is_leap_year(year):
#             return 29
#         else:
#             return 28
#     if month in (4, 6, 9, 11):
#         return 30
#     return 31

def get_day_by_month(year, month):
    if month < 1 or month > 12:
        return 0
    if month == 2:
        return 29 if is_leap_year(year) else 28
    if month in (4, 6, 9, 11):
        return 30
    return 31

print(get_day_by_month(2019,2))