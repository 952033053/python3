class Vehicle:
    def __init__(self,brand,speed):
        self.brand = brand
        self.speed = speed
class Electric_vehicle(Vehicle):
    def __init__(self,brand,speed,capacity,power):
        super().__init__(brand,speed)
        self.capacity=capacity
        self.power=power
v01 = Vehicle('兰博基尼',60)
e01 = Electric_vehicle('雅迪',90,1000,60)
print(v01.brand)
print(e01.brand)
