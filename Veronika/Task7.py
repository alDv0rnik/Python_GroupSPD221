text = input("Введите строку: ")
substring = input("Введите подстроку: ")

text = text.lower()
substring = substring.lower()

first_index = text.find(substring)
last_index = text.rfind(substring)

print(f"Индекс первого вхождения подстроки с начала строки: {first_index}")
print(f"Индекс последнего вхождения подстроки с конца строки: {last_index}")
