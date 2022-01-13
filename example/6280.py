n = int(input())

divisor = []
for i in range(n):
    if n % (i+1) == 0:
        divisor.append(i+1)

print(divisor)