data = []
words = input().split()
for word in words:
    if word not in data:
        data.append(word)

data.sort()

for word in data[:-1]:
    print(word, end=",")
print(data[-1])
