data_list1 = [1,3,6,78,35,55]
data_list2 = [12,24,35,24,88,120,155]
ans = []

for item in data_list2:
    if item in data_list1:
        ans.append(item)

print(ans)