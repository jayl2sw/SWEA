array = [2, 4, 6, 8, 10]

def find_number(n, array):
    if n in array:
        print("{} => True".format(n))
    else:
        print("{} => False".format(n))

print(array)
find_number(5,array)
find_number(10,array)

array = [2, 4, 6, 8, 10]

# def find_number(n, array):
#     x = [0] * 9999
#     for i in range(len(array)):
#         x[array[i]+1] += 1
#
#     if x[n+1] > 0:
#         return True
#     else:
#         return False
#
# print(array)
# print("5 => {}".format(find_number(5,array)))
# print("10 => {}".format(find_number(10,array)))