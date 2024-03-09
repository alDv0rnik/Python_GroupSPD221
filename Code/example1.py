# lst = [1, 2, 3, "test", "test1", True, [1, 2, 3, 4], {"a", "b"}, {"a": 1}]
lst = [1, 2, 3]
print(id(lst))
lst.append(4)
print(id(lst))
print(lst)
lst.append(8)
lst.append(5)
print(dir(lst))