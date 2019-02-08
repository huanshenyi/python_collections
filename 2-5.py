from random import randint,sample
"""方法1"""

"""sampleはデータの集合体から指定してる数の要素を取得"""
list = sample(['dd','dwdw','dwdd','dwdwdd','hii','dwdwddw','dwdw'],randint(3,6))
list_1 = {k: randint(1, 3) for k in sample(['太田', '鈴木', '川崎', '中山', '西村', '渡辺', '黒浜'], randint(3, 6))}
list_2 = {k: randint(1, 3) for k in sample(['太田', '鈴木', '川崎', '中山', '西村', '渡辺', '黒浜'], randint(3, 6))}
list_3 = {k: randint(1, 3) for k in sample(['太田', '鈴木', '川崎', '中山', '西村', '渡辺', '黒浜'], randint(3, 6))}
print(list_1)
print(list_2)
print(list_3)
# for k in list_1:
#     if k in list_2 and k in list_3:
#         print(k)
#
# list_4 = [k for k in list_1 if k in list_2 and k in list_3 ]
# print(list_4)

"""方法2"""
dl = [list_1, list_2, list_3]
# list_5 = [k for k in dl[0] if all(map(lambda d:k in d, dl[1:]))]
# print(list_5)


"""方法3 set的交集操作"""
s1 = list_1.keys()
s2 = list_2.keys()
s3 = list_3.keys()

s4=s1 & s2 & s3
print(s4)
"""かつ全ての得点も取得"""
for x in s4:
    print(x, (list_1[x]+list_2[x]+list_3[x]))


