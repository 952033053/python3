list01 = [1,4,8,9,12,20,]


def Even_numbers(item):
    return item % 2 == 0

def greater_than(item):
    return item > 10

def Between(item):
    return 10< item <50
def fun01(fon):
    for i in list01:
        if fon(i):
            yield i

for i  in fun01(greater_than):
    print(i)