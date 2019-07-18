"""
    参照day10/exercise02.py
    完成下列练习
"""
class SkillData:
    def __init__(self,id,name,atk_ratio,duration):
        self.id = id
        self.name = name
        self.atk_ratio = atk_ratio
        self.duration = duration
    def __str__(self):
        return '技能是：%s'%self.name

list_skill = [
    SkillData(101,"乾坤大挪移",5,10),
    SkillData(102,"降龙十八掌",8,5),
    SkillData(103,"葵花宝典",10,2),
]

fun01 = lambda item:len(item.name) > 4
fun02 = lambda item:item.id == 101
fun03 = lambda item:item.duration <= 5
from comn.list_helper import *
re = list_01().list_02(list_skill,fun01)
for i in re:
    print(i)