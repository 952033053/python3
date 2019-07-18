class Manager:
    def __init__(self):
        self.o01 = []
    def The_sum(self,wages):
         self.o01.append(wages)
    def Summation(self):
        a = 0
        for itme in self.o01:
            a += itme.calculation()
        return a

class Occupation:
    def __init__(self,Base):
        self.Base=Base
    def calculation(self):
        pass
class Programmer(Occupation):
    def __init__(self,Base,bonus):
        super().__init__(Base)
        self.bonus = bonus
    def calculation(self):
        return self.Base+self.bonus
class Sale(Occupation):
    def __init__(self,Base,money):
        super().__init__(Base)
        self.money = money
    def calculation(self):
        return self.Base+self.money*0.05
m01 = Manager()
m01.The_sum(Sale(3500,100000))
m01.The_sum(Programmer(5000,8000))
print(m01.Summation())

