# def sum_numbers(a, b):
#     res = a + b
#     return res


def sum_numbers(*args):
    res = sum(args)
    return res


r = sum_numbers(3, 5, 6, 8, 9, 1)

print(r)


def calculate_area(r, pi=3.14, flag=False):
    if flag:
        res = sum_numbers(r, pi)
        return res
    else:
        return pi * pow(r, 2)


print(calculate_area(5, flag=True))


values = {
    "a": 1,
    "b": 2,
    "c": 10
}


def get_another_sum(**kwargs):
    res = 0
    for k, v in kwargs.items():
        res += v
    return res


print(get_another_sum(a=1, b=2))
print(get_another_sum(**values))


def bar(a, b, c=0, *args, d=100, **kwargs):
    pass


bar(1, 3, 4, 5, 6, d=600, t=0, k="abc")


def func(*args, **kwargs):
    pass


# PEP 570
def get_sum(a, b, c, /):
    return a + b + c


# print(get_sum(a=1, b=2, c=3))

