class Enemy:
    def __init__(self,name,hp,atk):
        self.name = name
        self.hp = hp
        self.atk = atk
    @property
    def atk(self):
        return self.latk

    @property
    def hp(self):
        return self.__hp
    @hp.setter
    def hp(self,a):
        if 100 <= a <= 200:
            self.__hp = a
        else:
            print('血量输入有误')
    @atk.setter
    def atk(self,atk):
        if 10 <= atk <= 50:
            self.latk = atk

        else:
            print('攻击力输入有误')
    def print_int(self):
        print('%s,%d,%d' %(self.name,self.hp,self.atk))
a = Enemy('许',100,20)
print(a.print_int())
# print(a.print_int())