def find_longer(a, b):
    if len(a)>len(b):
        return a
    else:
        return b

n, m = input().split(',')
n = n.strip()
m = m.strip()

print(find_longer(n,m))