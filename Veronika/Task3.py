num = ""

while len(num) != 3 or not num.isdigit():
    num = input("Введите 3-х значное чило: ")

num = int(num)
digit1 = num // 100
digit2 = (num % 100) // 10
digit3 = num % 10

sum_of_digits = digit1 + digit2 + digit3

print(f"Сумма цифр числа {num} = {sum_of_digits}")
