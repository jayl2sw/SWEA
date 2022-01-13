def remove_duplication(list):
    ans = []
    for item in list:
        if item not in ans:
            ans.append(item)
    return ans


data_list1 = [12,24,35,24,88,120,155,88,120,155]

print(remove_duplication(data_list1))