data = input()

numbers = [0] * 26
for i in data:
    numbers[ord(i) - ord('a')] += 1

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
            'v', 'w', 'x', 'y', 'z']

for i in range(len(alphabet)):
    if numbers[i] != 0:
        print('{},{}'.format(alphabet[i], numbers[i]))


