L = [12, 24, 35, 70, 88, 120, 155]
ans = [i for i in L if L.index(i) != 0 and L.index(i) != 5 and L.index(i) != 4]
print(ans)
