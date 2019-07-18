class Xiaoming:
    def __init__(self,name):
        self.name =name
    @property
    def name(self):
        return self.__name
    @name.setter
    def name(self,value):
        self.__name = value
    def go_to(self,str_postion,type):
        print(self.name,'在',str_postion)
        type.run(str_postion)
class Car:
    def run(self,str_postion):
        print('')