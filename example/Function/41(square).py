def square(n):
    return n * n

n, m = map(int,input().split(','))

print("square({}) => {}".format(n,square(n)))
print("square({}) => {}".format(m,square(m)))