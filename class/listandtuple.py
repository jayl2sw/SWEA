data_list = [10, 21.5, "Python", True]
print("{} {}".format(type(data_list), data_list))

data_list = list(range(10, 21, 2))
print("{} {}".format(type(data_list), data_list))

data_str = list("안녕하세요")
print("{} {}".format(type(data_str), data_str))

data_list = [10, 20, 30, 40, 50]
print("data_list: {}".format(data_list))
for i in range(len(data_list)):
    print("data_list: {}".format(data_list[i]))

for i in range(len(data_list)):
    print("data_list: {}".format(data_list[-i-1]))

print("data_list[0:3] => {}".format(data_list[0:3]))

data_list1, data_list2 = [10,20,30], [40,50]
data_list = data_list1 + data_list2
print(data_list)


data_list1 = [1,2,3,4,5]
data_list7 = []
for x in data_list1:
    if x % 2 == 1:
        for y in data_list1:
            if y % 2 == 0:
                data_list7.append(x*y)

print(data_list7)