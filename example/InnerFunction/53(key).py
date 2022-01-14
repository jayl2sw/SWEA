array = 'abcdef'
index_array = list(enumerate(array))
for i in range(len(array)):
    print("{}: {}".format(index_array[i][1],index_array[i][0]))