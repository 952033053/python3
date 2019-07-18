# list01 = [3,4,55,6,7]
# def my_enumerate():
#     for item in enumerate(list01):
#         yield item
# for i,r in my_enumerate():
#     print(i,r)

# list02 = ['孙悟空','猪八戒','唐僧','沙僧']
# list03 = [101,102,103,104]
# def my_zip(*args):
#     for item in zip(list02,list03):
#         yield item
# for i in my_zip(0):
#     print(i)


list01 = [9,'五亿总探长','雷洛',0.25,95,0.5,'牛逼']
def Obtain():
    for item in list01:
        if type(item) == str:
            yield item
        if type(item) == float:
            yield item
for i in Obtain():
    print(i)
re = Obtain()
re01 = (item for item in list01 if type(item) == str)
for i in re01:
    print(i)
re02 = [item for item in list01 if type(item) == float]
for i in re02:
    print(i)
