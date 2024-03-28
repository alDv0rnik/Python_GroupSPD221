str = input('Enter str: ')
dct = {}

for ch in str:
    if ch in dct:
        dct[ch] += 1
    else:
        dct[ch] = 1
print(dct)
