n = int(input())
def fibo(number):
    if number == 0:
        return 1
    elif number == 1:
        return 1
    else:
        return fibo(number-1) + fibo(number-2)

array = []

for i in range(n):
    array.append(fibo(i))

print(array)