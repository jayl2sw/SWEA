numbers = []
for i in range(5):
    numbers.append(int(input()))

print("입력된 값 {}의 평균은 {}입니다.".format(numbers, sum(numbers)/5))
