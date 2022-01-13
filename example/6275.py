data = 'Python is powerful... and fast; plays well with others; runs everywhere; is friendly & easy to learn; is Open.'

answer = []

for alphabet in data:
    if alphabet != "a" and alphabet != "e" and alphabet != "i" and alphabet != "o" and alphabet != "u":
        answer.append(alphabet)

print(''.join(answer))
