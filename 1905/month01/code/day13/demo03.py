class Antitank_grenade:
    def explode(self):#实例方法需要通过self实例调用

    def __init__(self,hurt):
        self.hurt =hurt
class Thing(Antitank_grenade):
    def enemy(self,hp):
        print(self.hurt,'敌人',hp)
a01 = Antitank_grenade(' ')
t01 =  Thing('伤害')
print(t01.enemy(100))
