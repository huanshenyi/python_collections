from random import randint

"""方法1"""
"""リスト内の複数値を統計"""
data = [randint(0, 20) for _ in range(30)]
print(data)
# d = dict.fromkeys(data, 0)
# print(d)
"""dのvalを数分だけ+=1"""
# for x in data:
#     d[x] += 1
# print(d)
#
# x = sorted([(v,k) for k,v in d.items()],reverse=True)
# print(x)

"""方法2"""
from collections import Counter

d_1 = Counter(data)
print(d_1)
"""頻度最大トップ3"""
d_2 = d_1.most_common(3)
print(d_2)

"""文章の単語の数を数える"""
import re
txt = open('path').read()
txt_1 = re.split('\W+', txt)
txt_2 = Counter(txt_1)
txt_3 = txt_2.most_common(10)
print(txt_3)

