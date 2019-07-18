def print_list(l):
    for i in l:
        for r in i:
            print(r,end= ' ')
        print()
print_list([[1,2,3,44,],[4,5,5,5,65,6,87],[7,5]])

list01 = [
    [1,2,3,4],
    [5,6,7,8],
    [9,10,11,12],
    [13,14,15,16],
]
for i in range(len(list01)):
    for r in range(i,len(list01)):
            list01[i][r],list01[r][i] = list01[r][i],list01[i][r]
for a in list01:
    print(a)



