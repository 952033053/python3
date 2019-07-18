# list01 = [1,2,3,4,5]
# def map(list01):
#     list02 = []
#     list03 = []
#     for i in list01:
#         list02.append(i**2)
#     yield list02
#     for r in list02:
#         if r > 10:
#             list03.append(r)
#     yield list03
# for item in map(list01):
#     print(item)




# list01 = [{'name':'mocoy','age':18},{'name':'Adam','age':28}
#
#       ,{'name':'Talor','age':26},{'name':'Charlie','age':15}]
# for i in range(len(list01)):
#     for r in range(i+1,len(list01)):
#         if list01[i]['age'] > list01[r]['age']:
#             list01[i], list01[r] = list01[r], list01[i]
# print(list01)

# import time
# print(time.time())
# str_time01 = time.strftime("%Y-%m-%d %H:%M:%S",time.localtime())

list01 = [5,6,78,12,9,0,-1,2,3,-65,12]
list02 = []
for i in list01:
    if i not in list02:
        list02.append(i)
print(list02)

for i in range(len(list02)):
    for r in range(i+1,len(list02)):
        if list02[i] > list02[r]:
            list02[i], list02[r] = list02[r], list02[i]
print(list02)