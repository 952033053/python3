"""
字典
"""
# dict01 = {}
# while True:
#     a = input('输入商品名称:')
#     if a == ' ':
#         break
#     b = int(input('输入商品名称:'))
#     dict01[a] = b
# for key,value in dict01.items():
#     print('%s商品单价是%d' %(key,value))
#
# dict01 = {}
# while True:
#     a = input('输入商品名称:')
#     if a == ' ':
#         break
#     b = int(input('输入商品名称:'))
#     dict01[a] = b
# for key, value in dict01.items():
#     print('%s商品单价是%d' % (key, value))

# dict01 = {}
# while True:
#     a = input('输入学生姓名:')
#     if a == ' ':
#         break
#     age = int(input('输入年龄:'))
#     achievement = int(input('输入成绩:'))
#     gender = input('输入性别:')
#     dict01[a] = {'age':age,'achievement':achievement,'gender':gender}
# for name,dict_info in dict01.items():
#     print('姓名:%s 年龄:%d 成绩:%d 性别:%s' % (name,dict_info['age'],
#                                        dict_info['achievement'],
#                                        dict_info['gender']))
# dict_person_bobby = {}
# while True:
#     name = input("请输入姓名：")
#     if name == " ":
#         break
#     dict_person_bobby[name] = []
#     while True:
#         bobby = input("请输入喜好：")
#         if bobby == " ":
#             break
#         dict_person_bobby[name].append(bobby)
# print(dict_person_bobby)

# for name, list_bobby in dict_person_bobby.items():
#     print("%s喜欢%s：" % (name,list_bobby))
    # for item in list_bobby:
    #     print(item)


for i in range(10):
    for a in range(i+1):
        print(i*a)