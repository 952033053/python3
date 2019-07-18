class Wife:
    def __init__(self, name, age, weight):
        self.name = name
        # 本质:障眼法(实际将变量名改为：_类名__age)
        # self.__age = age
        self.set_age(age)
        # self.__weight = weight
        self.set_weight(weight)

    # 提供公开的读写方法
    def get_age(self):
        return self.__age

    def set_age(self, value):
        if 21 <= value <= 31:
            self.__age = value
        else:
            pass


    # 提供公开的读写方法
    def get_weight(self):
        return self.__weight

    def set_weight(self, value):
        if 40 <= value <= 60:
            self.__weight = value
        else:
            pass



w01 = Wife("铁锤公主", 20, 20)
# 重新创建了新实例变量(没有改变类中定义的__age)
# w01.__age = 107　
w01._Wife__age = 20  # (修改了类中定义的私有变量)

print(w01.__dict__)# python内置变量,存储对象的实例变量.


w01 = Wife("铁锤公主", 30, 50)
w01.set_age(25)
w01.set_weight(55)
print(w01.get_age())
print(w01.get_weight())

# 练习:定义敌人类(姓名，攻击力10 -- 50，血量100 -- 200)
#    创建一个敌人对象，可以修改数据，读取数据。
