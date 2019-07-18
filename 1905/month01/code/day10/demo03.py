class Laopo:
    w = 0
    @classmethod
    def print_count(cls):
        print('我有%d个老婆' %cls.w)
    def __init__(self,name,age):
        self.name = name
        self.age = age
        Laopo.w += 1
    def app(self):
        print('我老婆是：%s,她今年：%d 第%d个' %(self.name,self.age,Laopo.w))
Laopo('竹子',27)
Laopo('海红',24).app()

