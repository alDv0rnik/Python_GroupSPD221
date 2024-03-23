"""
Написать программу совпадения интересов 2-х пользователей

"""
user1 = ["кино", "книги", "шахматы", "плавание", "кулинария", "футбол"]
user2 = ["книги", "рыбалка", "автомобили", "игорные клубы", "футбол"]

common = set(user1).intersection(set(user2))
all_ = set(user1).union(set(user2))

result = len(common) / len(all_) * 100
print(round(result, 2))

