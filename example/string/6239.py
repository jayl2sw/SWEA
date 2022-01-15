data = input()

data_list = data.split(" ")

for i in range(len(data_list)):
    print(data_list[len(data_list)-1 -i], end= ' ')
