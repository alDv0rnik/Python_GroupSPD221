num = int(input("Введите число: "))

if num == 0:
    print("Это ноль")
elif num > 0:
    num_length = len(str(num))
    print(f"{num} - положительное число, кол-во разрядов: {num_length}")
else:
    num_length = len(str(num)) - 1
    print(f"{num} - отрицательное число, кол-во разрядов: {num_length}")
