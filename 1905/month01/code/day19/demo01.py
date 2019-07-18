# def verify_permissions(func):
#     def wrapper(*args, **kwargs):
#         print("验证账户")
#         func(*args, **kwargs)
#     return wrapper
# @verify_permissions
# def deposit(money):
#     print('存%d钱'%money)
# @verify_permissions
# def withdraw(login_id,pwd):
#     print('取钱',login_id,pwd)
# deposit(10000)
# withdraw('zs',123)
def verify_permissions(func):
    def wrapper(*args, **kwargs):
        print("验证账户")
        func(*args, **kwargs)
    return wrapper
import time
@verify_permissions
def fun01():
    time.sleep(2)
    print('fun01执行完毕')
@verify_permissions
def fun02(a):
    time.sleep(1)
    print('fun02执行完毕',a)
fun01()
fun02(100)