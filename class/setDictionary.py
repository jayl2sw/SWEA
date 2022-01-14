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
    "홍길동" : 20,
    "이순신" : 45,
    "강감찬" : 35,
}
print(data_dict1)

#키를 문자열로 적지 않는다.
data_dict2 = dict(홍길동 = 20, 이순신 = 45, 강감찬 = 35)
print(data_dict2)

data_tuple1 = (("홍길동", 20), ("이순신", 45), ("강감찬", 35))
data_dict3 = dict(data_tuple1)

data_list1 = [("홍길동",20), ("이순신", 45), ("강감찬", 35)]
data_dict4 = dict(data_list1)

data_dict5 = {key : data_dict1[key] for key in data_dict1}
data_dict6 = {key : data_dict1[key] for key in data_dict1.keys()}
print(data_dict5)
print(data_dict6)

data_dict7 = {item[0]: item[1] for item in data_dict1.items()}
print(data_dict7)

# 13-17

scores = []
NoStudents = int(input("총 학생의 수를 입력하세요: "))

for i in range(1, NoStudents +1):
    score = {}
    score["name"] = input("학생의 이름을 입력하세요: ")
    score["kor"] = int(input("{} 학생의 국어 점수를 입력하세요: ".format(score['name'])))
    score["mat"] = int(input("{} 학생의 수학 점수를 입력하세요: ".format(score['name'])))
    score["eng"] = int(input("{} 학생의 영어 점수를 입력하세요: ".format(score['name'])))
    scores.append(score)

for score in scores:
    total = 0
    for key in score:
        if key != 'name':
            total += score[key]
    print("{} => 총점: {}, 평균 {}".format(score["name"], total, total/3))
    average = total / 3

kor_total, mat_total, eng_total = 0, 0, 0

for score in scores:
    for key in score:
        if key == "kor" :
            kor_total += score[key]
        elif key == "mat":
            mat_total += score[key]
        elif key == "eng":
            eng_total += score[key]

print(kor_total, kor_total/NoStudents)
print(mat_total, mat_total/NoStudents)
print(eng_total, eng_total/NoStudents)