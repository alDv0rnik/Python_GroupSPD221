dct = {
    'a': 1,
    'b': 2,
    'c': 3,
    'd': 4,
    'e': 5,
    'f': 6
}

keys = list(dct.keys())
dct[keys[0]], dct[keys[-1]] = dct[keys[-1]], dct[keys[0]]

del dct[keys[1]]

dct['new_key'] = 'new_value'
print(dct)
