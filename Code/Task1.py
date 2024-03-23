"""
Проверить слова на анаграммы

кластер
стрелка
сталкер
"""

str1, str2, str3 = input(), input(), input()

if len(str1) != len(str2) and len(str1) != len(str3):
    print(False)
else:
    print(True if set(str1) == set(str2) == set(str3) else False)