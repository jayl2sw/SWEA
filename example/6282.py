list = [1, 3, 11, 15, 23, 28, 37, 52, 85, 100]
result = []

for item in list:
    if item % 2 == 0:
        result.append(item)

print(result)