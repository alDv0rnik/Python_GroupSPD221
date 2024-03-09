l1 = []
l2 = list()

l2 = l1

# print(id(l1))
# print(id(l2))

l = [1, 2, 3, 4, 5]
# print(l[2:])
# print(l[:])

l[0] = "a"
print(l)

l3 = [1, 2, [3, 4, 5]]
# print(l3[2])
# print(l3[2][1])

l2d = [[1, 2],[3, 4]] # numpy
print(len(l))
l[7:7] = "b"
# l[6:6] = "b"
print(len(l))

# print(l[7])

l[2:5:2] = "v", "c"
print(l)

print(id(l[1]), id(2))