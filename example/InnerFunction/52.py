
def max2(*arg):
    max = -99999999
    for i in arg:
        if max < i:
            max = i
    return max

print("max(3, 5, 4, 1, 8, 10, 2) => {}".format(max2(3,5,4,1,8,10,2)))

