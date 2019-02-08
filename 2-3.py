from random import randint

d = {k: randint(60, 100) for k in 'abcdefg'}
print(d)
l = [(v, k) for k, v in d.items()]
print(l)
new_l = sorted(l, reverse=True)
print(new_l)

# z =list(zip([1, 2, 3], [4, 5, 6]))
# print(z)

# z = list(zip(d.values(), d.keys()))
# z_new = sorted(z,reverse=True)
# print(z)
#
# print(z_new)

# x = sorted(d.items(), key=lambda i: i[1], reverse=True)
# print(x)
# xx = list(enumerate(x, 1))
# print(xx)
# yy = []
# for i, (k, v) in enumerate(x, 1):
#     yy.append({
#         k: (i, v)
#     })
#     print(i, k, v)
# print(yy)

# m={k:(i,v) for i,(k,v) in enumerate(x,1)}
# print(m)

# list_x = {k: randint(60,100) for k in 'abcdefg'}
#
# list_y =[(v,k) for k,v in list_x.items()]
# print(list_y)
#
# list_m = sorted(list_y,reverse=True)
# print(list_m)



