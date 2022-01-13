data_list = [(90,80), (85,75), (90,100)]
for i in range(len(data_list)):
    total = 0
    for j in range(len(data_list[i])):
        total += data_list[i][j]
    print("{}번 학생의 총점은 {}점이고, 평균은 {}입니다.".format(i+1, total, total/2))