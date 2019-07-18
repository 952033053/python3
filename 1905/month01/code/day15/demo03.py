# def div_apple(apple_count):
#     while True:
#         try:
#             person_count = int(input(':'))
#         except Exception:
#             print("出错喽")
#             continue
#         result = apple_count / person_count
#         print("每人%d个苹果"%result)
# try:
#     div_apple(10)
# except Exception:
#     print("出错喽")
#
def get_score():
    # while True:
        str_result = input(':')
        score = int(str_result)
        if 0 <= score <= 100:
            print(score)
            return True
        else:
            print("超过范围")
while True:
    try:
        if get_score():
            break
        # get_score()
    except:
        print('输入错误，重新输入')
    # if get_score():
    #     break