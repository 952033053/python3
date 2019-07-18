str01 = ' 校 训: 自 强不息,厚德载物.   '


def method_name():
    global int02

    def int02(str01, a):  # 计算空格个数
        l1 = []
        for i in str01:
            if i == a:
                l1.append(i)
        return len(l1)


method_name()

#删除空格
print(str01.strip())
print(str01.replace(' ',''))
str01 = str01.replace(' ','')
if str01[0:2] == '校训':
    print('是已校训开头的')
else:
    print('不是已校训开头的')
#
import math
def is_prime(num):
	for i in range(2,int(math.sqrt(num)+1)):
		if num%i == 0:
			return False
	return True
prime = []
for i in range(2,101):
    if is_prime(i):
        prime.append(str(i))
print(' '.join(prime))

def int01(a):
    for i in range(a):
        for r in range(2,i):
            if i % r == 0:
                return False
        else:
           return True

a = '  许sa dsd1 a1 许1a1s许d   '

print(int02(a,'d'))
print(int01(100))
print(method_name())
print(is_prime(10))