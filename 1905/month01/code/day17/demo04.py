class SkillData:
    def __init__(self,name,aggressivity,defense,blood):
        self.name = name
        self.aggressivity = aggressivity
        self.defense = defense
        self.blood = blood
    def __str__(self):
        return '姓名是：%s'%self.name

list_skill = [
    SkillData("旋涡鸣人",100,90,5000),
    SkillData("宇智波佐助",105,88,4900),
    SkillData("宇智波班",120,108,6900),
    SkillData("灭霸",66,69,0),
    SkillData("旗木卡卡西",80,72,5900),
    SkillData("蒙奇Ｄ路飞",59,109,3800),
    SkillData("罗罗诺亚索隆",120,105,7800),
]

# fun01 = lambda item:item.name == "灭霸"
# fun02 = lambda item:item.aggressivity > 100
# fun03 = lambda item:item.blood > 0
# from comn.list_helper import *
# re = list_01().list_02(list_skill,fun03)
# for i in re:
#     print(i)

# fun01 = lambda item:"灭霸" == item.name
# fun02 = lambda item:item.aggressivity > 130 or item.defense > 110
fun01 = lambda blood:blood
from comn.list_helper import *
re = list_01().list_02(list_skill,fun01)
for i in re:
    print(i)

# re = list_01().list_02(list_skill,fun01)
# print(re)
