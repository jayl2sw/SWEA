array = [1, 2, 3, 4, 3, 2, 1]
# def find_onlyone(array):
#     x = [0] * 5
#     for i in range(len(array)):
#         x[array[i]] += 1
#
#     onlyone = []
#     for i in range(len(x)):
#         if x[i] > 0:
#             onlyone.append(i)
#     return onlyone


# def find_onlyone(array):
#     onlyone = []
#     for i in range(len(array)):
#         if array[i] not in onlyone:
#             onlyone.append(array[i])
#     return onlyone
#
#
# print(find_onlyone(array))

def find_onlyone(array):
    x = [0] * 5
    for i in range(len(array)):
        x[array[i]] += 1

    onlyone = []
    for i in range(len(x)):
        if x[i] == 1:
            onlyone.append(i)
    return onlyone

new_array=[]
def function():
    for i in array:
        if i not in new_array:
            new_array.append(i)
    print(new_array)
    return

print(array)






