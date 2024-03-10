s = "it_step_course"

words = s.split("_")

s = words[0]
for word in words[1:]:
    s += word.replace(word[0], word[0].upper())

print(s)
