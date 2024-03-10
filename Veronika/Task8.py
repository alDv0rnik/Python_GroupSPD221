s = input("Введите строку: ")

space_count = s.count(" ")
non_space_count = len(s.replace(" ", ""))

print(f"Количество пробелов: {space_count}, количество других символов: {non_space_count}")