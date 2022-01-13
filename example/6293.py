from math import pi
list = list(map(int, input().split(',')))

ans = []
for item in list:
    ans.append(item * 2 * pi)

for j in ans[:-1]:
    print("{:.2f}".format(j), end=', ')

print("{:.2f}".format(ans[-1]))

