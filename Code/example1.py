import sys

set_ = set()
d = {}
# print(type(set_))

print(sys.getsizeof(set_))
print(sys.getsizeof(d))

# set_.pop()

s = "test_string"
set_ = set(s)
# nums = {1, 2, 3, 4, 5}
# print(set_[0])
# print(nums)

i = set_.pop()
print(i)

# DISCARD, REMOVE
print(set_)
set_.discard('t')
print(set_)
set_.discard('t')

# set_.remove('a')

# print(dir(set_))

# for i in set_:
#     print(i)

set_1 = {1, 2, 3, 4, 5}
set_4 = {1, 2, 3, 4, 5}
set_2 = {6, 7, 8, 9, 10}
set_3 = {1, 2, 5}

# set_1.update(set_2)
# set_1 |= set_2

print(set_1.union(set_2))
print(set_1 & set_3)

print(set_1 | set_3)

# print(set_1.difference(set_3))
# print(set_3.difference(set_1))
# print(5 in set_1)
#
# print(set_1.intersection(set_3))
# print(set_1 - set_3)


# COMPARISON

# print(set_1 > set_3)
# print(set_3 > set_1)
# print(set_1 == set_4)

# print(set_3.issubset(set_1))
# print(set_1.issuperset(set_3))
# print(set_1.isdisjoint(set_2))

# ADD

set_1.add("a")
set_1.add("z")
set_1.add("z")
# print(set_1)

fs = frozenset([1, 2, 3, 4, 5])
# print(fs)
# fs.discard(1)
# fs.add(6)

