# def second01(second):
#     hour = second//3600
#     minute = second // 60 % 60
#     second = second % 60
#     return hour,minute,second
# re = second01(10000)
# print('小时:'+str(re[0])+'分钟:'+str(re[1])+'秒:'+str(re[2]))

# def shu(args):
#     args[0],args[1]=args[1],args[0]
#     return args
# a = 0
# print(a)=,
# l = [1,2,3]
# c = [7,8,9]
# a = 0
# print(a)
# print(shu(l))
# print(shu(c))
def fun01():
    name = 1
    print(name)
    move_right()


list_merge = [1,5,9]
def move_right():
    global list_merge
    list_merge = list_merge[::-1]
    print(list_merge)
fun01()
