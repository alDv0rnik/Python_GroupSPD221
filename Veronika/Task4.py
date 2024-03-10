import math

x1 = float(input("Введите координату x1: "))
y1 = float(input("Введите координату y1: "))
x2 = float(input("Введите координату x2: "))
y2 = float(input("Введите координату y2: "))

distance = math.sqrt((x2 - x1)**2 + (y2 - y1)**2)

print(f"Расстояние между a({x1}, {y1}) и b({x2}, {y2}) = {distance}")
