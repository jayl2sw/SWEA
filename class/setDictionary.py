# 셋 내포

data_set1 = {1, 2, 3, 4, 5}
print("data_set1: {0}, {1}".format(type(data_set1), data_set1))

data_set2 = {item for item in data_set1}
print("data_set2: {0}, {1}".format(type(data_set2), data_set2))

data_set3 = {item for item in data_set1 if item % 2 == 1}
print("data_set3: {0}, {1}".format(type(data_set3), data_set3))

# 셋 변환
data_str = "Hello"
data_list = list(data_str)
print(data_list)
data_tuple = tuple(data_list)
data_set = set(data_tuple)
data_list = list(data_set)
print(data_tuple)
print(data_set)
print(data_list)

# 딕셔너리
data_dict1 = {
    "홍길동": 20,
    "이순신": 45,
    "강감찬": 35,
}
print(data_dict1)

data_dict2 = dict(홍길동=20, 이순신=45, 강감찬=35)
print(data_dict2)
