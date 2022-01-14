numbers = list(map(int, input().split(', ')))
ans = [i for i in numbers if numbers.index(i) % 2 == 0]

for i in ans[:-1]:
    print(i, end= ', ')
print(ans[-1])
