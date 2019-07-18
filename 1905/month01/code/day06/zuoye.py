l = []
for i in range(1970,2051):
    if i % 4 == 0 and i % 100 != 0 or i % 400 == 0:
        l.append(i)
print(l)

scenicspot = {'北京':{'景区':['故宫,天安门,天坛'],'美食':['烤鸭,炸酱面,豆汁,卤煮']}
              ,'四川':{'景区':['九寨沟,峨眉山,春熙路'],'美食':['火锅,串串香,兔头']}}
# for i,a in scenicspot.items():
#     print(i+':')
#     for b,p in a.items():
#         m = ''.join(p)
#         print(' '*(len(i)+1) + b+':'+m)

for i in scenicspot:
    print(i+':')
    for b,p in scenicspot[i].items():
        m = ''.join(p)
        print(' '*(len(i)+1) + b+':'+m)

