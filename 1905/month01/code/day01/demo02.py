'''
bool
运算符
    比较运算符:
> < >= <= == !=(不等于)
    逻辑运算符:判断两个bool值关系
         与 或 非
'''
# bool 类型
# 取值 : (真,对的)true  (假,错的)false
# 命题: 带有判断性的陈述句.

year = int(input('输入年份:'))
a = year % 4 == 0 and year % 100 != 0 or year % 400 == 0
print(a)
