while True:
    quarter = input('请输入季度:')

    if quarter == '春':
        print('春季为1月,2月,3月')
    elif quarter == '夏':
        print('夏季为4月,5月,6月')
    elif quarter == '秋':
        print('秋季为7月,8月,9月')
    elif quarter == '东':
        print('东季为10月,11月,12月')
    if input('按e退出:') == 'e':
        break
    else:
        print('您输入的指令有误')

# number = float(input('请输入一个数字:'))
# operator = input('请输入一个运算符:')
# number01 = float(input('请输入第二个数字:'))
# if operator == '+':
#     print(number + number01)
# elif operator == '-':
#     print(number - number01)
# elif operator == '/':
#     print(number / number01)
# elif operator == '*':
#     print(number * number01)
# else:
#     print('运算符错误')

# l = []
# number = float(input('请输入一个数字:'))
# number01 = float(input('请输入第二个数字:'))
# number02 = float(input('请输入第三个数字:'))
# number03 = float(input('请输入第四个数字:'))
# l.append(number)
# l.append(number01)
# l.append(number02)
# l.append(number03)
# a = max(l)
# print(a)
# if number > number01 and number > number02 and number > number03:
#     print('最大的是:' + str(number))
# elif number01 > number and number01 > number02 and number01 > number03:
#     print('最大的是:' + str(number01))
# elif number02 > number01 and number02 > number and number02 > number03:
#     print('最大的是:' + str(number02))
# elif number03 > number01 and number03 > number02 and number03 > number:
#     print('最大的是:' + str(number03))
# elif number03 == number01  == number02 == number:
#     print('恭喜你习提豹子')
# else:
#     print('输入有误')
# max_number = number
# if max_number < number01:
#     max_number = number01
# if max_number < number02:
#     max_number = number02
# if max_number < number03:
#     max_number = number03
# print('最大的是:',max_number)