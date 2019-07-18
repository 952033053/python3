# class Dog():
#
#     def __init__(self, name, age):
#
#         self.name = name
#         self.age = age
#     def sit(self):
#
#         print(self.name.title() + " is now sitting.")
#     def roll_over(self):
#
#         print(self.name.title() + " rolled over!")
# my_dog = Dog('大白', 6)#self=Dog('大白', 6)  self=my_dog
# print("我的小狗叫 " + my_dog.name + ".")
# print("今年它 " + str(my_dog.age) + " 岁了.")
# my_dog.sit()
# my_dog.roll_over()

# class Car():
#     def __init__(self, make, model, year):
#
#         self.make = make
#         self.model = model
#         self.year = year
#     def get_descriptive_name(self):
#
#         long_name = str(self.year) + ' ' + self.make + ' ' + self.model
#         return long_name.title()
# my_new_car = Car('audi', 'a4', 2016)
# a = Car('许','兵',2017)
# print(my_new_car.get_descriptive_name())
# print(a.get_descriptive_name())

class Mobile_phone():
    # 手机品牌，型号，内存
    def __init__(self, brand, model, memory):
        self.brand = brand
        self.model = model
        self.memory = memory

    def style(self):
        phone = '手机品牌：' + self.brand + ',手机型号：' + self.model + ',手机内存：' + self.memory + '.'
        return phone
oppo = Mobile_phone('oppo', 'r9', '128g')
vivo = Mobile_phone('vivo', 'x9', '64g')
apple = Mobile_phone('apple', 'xs', '256g')
huawei = Mobile_phone('huawei', 'p30', '128g')
print(oppo.style())
print(vivo.style())
print(apple.style())
print(huawei.style())




