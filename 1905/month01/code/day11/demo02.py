class Enemy:
    def __init__(self,name,hp,atk):
        self.name = name
        self.e03(hp)
        self.e04(atk)
    def e01(self):
        return self.atk
    def e02(self):
        return self.hp
    def e03(self,hp01):
        if 100 <= hp01 <= 200:
            self.hp = hp01
        else:
            print('血量输入有误')
    def e04(self,atk):
        if 10 <= atk <= 50:
            self.atk = atk

        else:
            print('攻击力输入有误')
a = Enemy('许',300,20)
print(a.name)
# print(a)
print(a.e02())
print(a.e04(40))
print(a.__dict__)