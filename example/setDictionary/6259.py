# data = input()
# set_letter = set({})
# set_digit = set({})
#
# for i in range(len(data)):
#    if 57 >= ord(data[i]) >= 48 :
#        set_digit.add(data[i])
#    else :
#        set_letter.add(data[i])
#
# print('LETTERS {}'.format(len(set_letter)))
# print('DIGITS {}'.format(len(set_digit)))




T = input().strip()
a=0
b=0
for i in T:
    if 'a' <= i <= 'z' or 'A' <= i <= 'Z':
        a += 1
    elif '0' <= i <='9':
        b += 1
print("LETTERS %d" % a)
print("DIGITS %d" % b)


