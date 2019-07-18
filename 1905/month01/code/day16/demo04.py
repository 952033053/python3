def num(dict01):
    for i in dict01:
        yield i,dict01[i]
#return只返回第一个值，程序就结束，下次重新调用就是重新开始
#yield函数程序不会结束，下一次调用会继续下一步，自动生成迭代
#对象跟迭代器__next__()


dict01 = {'牛魔王':100,'孙悟空':300,'铁三公主':150}
for i in num(dict01):
    print(i)
    print(i[0])
#打印结果：('牛魔王', 100)
'''
('牛魔王', 100)
牛魔王
('孙悟空', 300)
孙悟空
('铁三公主', 150)
铁三公主
'''