# class Student:
#     def __init__(self,name,age,score,sex):
#         self.name = name
#         self.age = age
#         self.score = score
#         self.sex = sex
#     def information(self):
#         print('姓名:'+self.name+',年龄：'+str(self.age)+
#         ',成绩:'+str(self.score) +',性别:'+self.sex)
# l = []
# while True:
#     name = input('请输入姓名:')
#     if name == ' ':
#         break
#     age = int(input('请输入年龄:'))
#     score = int(input('请输入成绩:'))
#     sex = input('请输入性别:')
# l.append(Student(name,age,score,sex))
# for i in l:
#     i.information()
# l[0].information()

class Student:
    def __init__(self, name, age, score, sex):
        self.name = name
        self.age = age
        self.score = score
        self.sex = sex

    def print_self_info(self):
        print("%s的年龄是%d,成绩是%d,性别是%s" % (self.name, self.age, self.score, self.sex))

list_student_info = []
while True:
    name = input("请输入姓名：")
    if name == " ":
        break
    age = int(input("请输入年龄："))
    score = int(input("请输入成绩："))
    sex = input("请输入性别：")
    # stu = Student(name, age, score, sex)
    list_student_info.append(Student(name, age, score, sex))

for i in list_student_info:
    i.print_self_info()
# 获取第一个学生信息
# info = list_student_info[0]
list_student_info[0].print_self_info()
