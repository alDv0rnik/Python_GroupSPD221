m = int(input('Введите кол-во продуктов в кладовой: '))
n = int(input('Введите кол-во необходимых ингредиентов: '))

products = set()

for _ in range(m):
    product = input('Введите продукт: ').strip().lower()
    products.add(product)

for _ in range(n):
    ingredient = input('Введите ингредиент: ').strip().lower()
    if ingredient in products:
        print("Есть")
    else:
        print("Отсутствует")
