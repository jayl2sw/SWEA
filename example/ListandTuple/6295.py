n, m = map(int, input().split(','))
ans = []
for i in range(n):
    milestone = []
    for j in range(m):
        milestone.append(i * j)
    ans.append(milestone)

print(ans)