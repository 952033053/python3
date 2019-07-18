# def list_01(list01):
#     for r in range(len(list01)-1):
#         for c in range(r+1,len(list01)):
#             if list01[r] > list01[c]:
#                 list01[r],   list01[c]=   list01[c], list01[r]
#
# list01 = [43,4,5,6,7]
# list_01(list01)
# print(list01)
a = 100
def list_01(list01):
    '''
    方阵转置
    :param list01:
    :return:
    '''
    a = 100
    for c in range(1,len(list01)):
        for r in range(c,len(list01)):
            list01[r][c-1],list01[c-1][r]=list01[c-1][r],list01[r][c-1]

list01 = [[1,2,3,4],
[5,6,7,8],
[9,10,11,12],
[13,14,15,16]
]
list_01(list01)
for i in list01:
    print(i)
print(a)