s = input()
dct = {}

for digit in s:
    if digit.isdigit():
        digit = int(digit)
        dct[digit] = dct.get(digit, 0) + 1

res = {}
for _ in range(3):
    max_count = max(dct.values())
    max_digit = [digit for digit, count in dct.items() if count == max_count]
    res[max_digit[0]] = max_count
    del dct[max_digit[0]]

print(res)
