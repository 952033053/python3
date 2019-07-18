
class Asadf:
    def __init__(self):#这里的行参是可以变换的
        #__init__把实例变量都绑定在self，可以在类方法使用．
        # 如果不使用__init__，方法无法使用实例变量
        self.a = 100 #这里的实例变量是固定的．构造函数
    def asdasd(self):
        print(self.a)
a = Asadf()
a.asdasd()