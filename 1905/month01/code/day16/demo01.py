list01 = ('铁扇公主','铁锤公主','扳手王子').__iter__()
while True:
    try:
        item = list01.__next__()
        print(item)
    except StopIteration:
        break
        #迭代器就是访问对象的工具，也就是用__iter__()方法实现
dict02 = {'铁扇公主':101,'铁锤公主':102,'扳手王子':103}
dict01 = dict02.__iter__()
while True:
    try:
        item = dict01.__next__()
        print(item,dict02[item])
    except StopIteration:
        break

