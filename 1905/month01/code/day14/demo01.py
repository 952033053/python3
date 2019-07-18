class Enemy:
    def __init__(self,name,hp,atk):
        self.name = name
        self.hp = hp
        self.atk = atk
    # def __str__(self):
    #     return "我叫%d,编号是%s,年龄是%d" \
    #            % (self.name, self.hp, self.atk)

    # def __repr__(self):
    #     return "Enemy(%d,'%s',%d)" %(self.name,self.hp,self.atk)
e01 = Enemy(15,'12',1000)
str01 = repr(e01)
print(str01)
print(e01)
print(eval(str01))


# class Vector1:
#     def __init__(self,x):
#         self.x = x
#     def __str__(self):
#         return '数学运算:'+str(self.x)
#     def __add__(self, other):
#         return Vector1(self.x + other)
#
# v01 = Vector1(10)
# a= v01 + 3
