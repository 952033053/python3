class Student:
    #name是行参
    def __init__(self,name#数据):
        self.name = name
        #  name是属性或者类变量
    @property#属性
    def name(self):
        return self.__name#这是实例变量
    @name.setter
    def name(self,b):
        self.__name = b#这个只能在类中使用
a = Student('XU')
print(a.name)#访问类变量
#数据不同可以放一个类中，做对象
#比如def print_int(setter,name对象参数)