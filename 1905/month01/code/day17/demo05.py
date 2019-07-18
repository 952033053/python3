# list02 = ['孙悟空','猪八戒','唐僧','沙僧']
# list03 = [101,102,103,104]
# def my_zip2(*args):
#     # 根据星号元组形参args第一个参数的长度生成索引len(args[0])
#     for i in range(len(args[0])):
#         list_result = []
#         for item in args:
#             list_result.append(item[i])
#         yield tuple(list_result)
#
# for item in my_zip2(list02,list03):
#     print(item)
list01 = [1,2,3,4,5]
list01 = [i**2 for i in list01]
print(list01)
list01 = [i for i in list01 if i > 10]
print(list01)