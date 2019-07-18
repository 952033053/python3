class Shang_pin_info:
    __init_id = 1
    '''
    商家添加商品
    '''
    def __init__(self,name,price,id=1):
        self.id = id
        self.name = name
        self.price = price
        self.__list01 = []
    def ad__(self,commodity):
        self.__list01.append(commodity)
    def generate_id(self):
        Shang_pin_info.__init_id += 1
        return Shang_pin_info.__init_id
class input_commodity:
    def __init__(self):
        pass
    def main(self):
        while True:
            self.__input_student()

    def __input_student(self):
        name = input('请输入商品名称:')
        price = int(input('请输入商品价格:'))
        stu = Shang_pin_info(name,price)
        s = {'id':stu.generate_id,"name":name,"price":price}





