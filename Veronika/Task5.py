correct_answers = {
    1: 'A',
    2: 'B',
    3: 'C',
    4: 'D'
}
user_answers = ['B', 'B', 'A', 'D']

score = 0

for question, user_answer in enumerate(user_answers, start=1):
    correct_answer = correct_answers.get(question, None)
    if correct_answer is not None and user_answer == correct_answer:
        score += 1

print({'score': score, 'correct_answers': list(correct_answers.values())})
