import sys

t = ()
l = []
t1 = ()
l2 = list()

# print(id(t))
# print(id(t1))
# print(id(l))
# print(id(l2))
#
# print(l.__sizeof__())
# print(t.__sizeof__())
#
# print(sys.getsizeof(t))
# print(sys.getsizeof(l))


t2 = (1, 2, 3)
print(id(t2))
del t2

t3 = (1, 2, 3)
print(id(t3))