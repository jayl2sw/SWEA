a = [1,1]

for i in range(8):
    a.append(a[i]+a[i+1])

print(a)