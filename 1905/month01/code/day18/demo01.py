list01 = ([1,1,1],[2,2],[3,3,3,3])
re = min(list01,key=lambda item: len(item))
print(re)
# for i in re:
#     print(i)
list02 = [1,9,78,34,11]
re = filter(lambda item: item > 10, list02)
for i in re:
    print(i)
re = sorted(list02, key=lambda item: item,reverse=True)
for i in re:
    print(i)
re = map(lambda item: item, list02)
for item in re:
    print(item)