class Student:
    def __init__(self, name, age, score, sex):
        self.name = name
        self.age = age
        self.score = score
        self.sex = sex

    def print_self_info(self):
        print("%s的年龄是%d,成绩是%d,性别是%s" % (self.name, self.age, self.score, self.sex))

list01 = [Student('许', 31, 100, '女'),
          Student('念', 26, 90, '男'),
          Student('兵', 29, 80, '女'),
          Student('老苏', 32, 70, '男')]
# while True:
#     name = input("请输入姓名：")
#     if name == " ":
#         break
#     age = int(input("请输入年龄："))
#     score = int(input("请输入成绩："))
#     sex = input("请输入性别：")
#     # stu = Student(name, age, score, sex)
#     list_student_info.append(Student(name, age, score, sex))

# for i in list_student_info:
#     i.print_self_info()
# # 获取第一个学生信息
# # info = list_student_info[0]
# list_student_info[0].print_self_info()
def find01():
    for i in list01:
        if '老苏' == i.name:
            return i
print(find01().name,find01().age)
def find02():
    l = []
    for i in list01:
        if '女' == i.sex:
           print(i.name,i.score)
find02()
def find03():
    a = 0
    for i in list01:
        if i.age >= 30:
             a += 1
    return a
print(find03())
def find04():
    for i in list01:
        i.score = 0
find04()
# def find05():
#     for i in range(len(list01)):
#         print(list01[i].name)
# find05()
def find06():
    max_stu = list01[0]
    for i in range(1,len(list01)):
        if max_stu.age < list01[i].age:
            max_stu = list01[i]
    return  max_stu
find06().print_self_info()



