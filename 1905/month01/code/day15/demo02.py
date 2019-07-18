import time
# def time09(a,b,c):
#     str_time01 = time.strftime('%d-%d-%d'%(a,b,c))
#     print(str_time01)
# time09(2019,6,15)
# str_time01 = time.strftime("%Y / %m / %d %H:%M:%S", time.localtime())
# print(str_time01)
# print(time.localtime())
# 3. 时间元组 -->  str
print(time.strftime("%Y / %m / %d %H:%M:%S", time.localtime()))
print(time.strptime('2018/2/10', "%Y/%m/%d"))
print('一个个长的跟盆似的，还那么多要求，你配吗？')
import time


def life_days(year, month, day):
    """
        根据生日计算活了多少天
    :param year: 年
    :param month: 月
    :param day: 日
    :return: 活的天数
    """
    tuple_time = time.strptime("%d-%d-%d" % (year, month, day), "%Y-%m-%d"#时间元组)
    life_second = time.time() - time.mktime(tuple_time)
    return int(life_second / 60 / 60 // 24)


print(life_days(1998, 5, 19))