# #一个球从100米高空落下,每次弹起是落下的一半.
# #计算一共弹了多少次?(最低弹起高度0.01)
# #一共走了多少米?
#
# height = 100
# count = 0
# distance = height
# while height / 2  > 0.01:
#     count += 1
#     height /= 2
#     print(height)
#     distance += height*2
#
# print(count)
# print(distance)
# print('总共经过%.2f' %distance)

list01 = ['我是齐天大圣']
索引:
print(list01[2]) #齐
切片:
print(list01[-4:])#齐天大圣
追加(在末尾添加):
list01.append('八戒')
插入(在指定位置添加)
list01.insert(1,true)
删除元素
根据元素删除
list01.remove('是')
根据位置删除
del list01[0]

定义元素,目的,可以增删改查元素.
切片
del list01[1:3]
list01[1:3] = ['a','b'] #1到3之间添加
list01[1:3] = [] #1到3之间删除
