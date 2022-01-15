# data_str = "와우! 안녕하세요, 파이썬입니다."
#
# start = input("시작 인덱스를 입력하세요: ")
# end = input("종료 인덱스를 입력하세요: ")
#
# try:
#     start = int(start)
# except ValueError:
#     start = None
#
# try:
#     end = int(end)
# except ValueError:
#     end = None
#
# print("{}".format(data_str[start:end]))
#
# data_str = "Have a nice day!"
# input_str = "nice"
# print(data_str.count(input_str))
#
# idx = data_str.find(input_str)
# print(idx)

# data_str = "가나다라마바사아자차카타파하"
# comma_space = ", "
#
# output = comma_space.join(data_str)
# print(output)


# data_str =  "10, 20, 3o, 40, 50"
#
# data_str = data_str.replace(" ", "")
# print(data_str)
#
# data_list = data_str.split(",")
# for val in data_list:
#     print(val, end=" ")
#     if not val.isdigit(): # 숫자일 때, True를 반환한다.
#         print("<= ", end="")
#     print()

# 14-14
data_str = "파이썬은 클래스를 이용해 객체를 생성하는 객체지향 프로그래밍 언어입니다."

mask_str = input("마스킹할 문자열을 입력하세요:")
find_str = input("찾을 문자열을 입력하세요:")
idx = -1
count = 0
while True:
    idx = data_str.find(find_str, idx + 1)
    if idx != -1:
        print("[{0}] ~ [{1}]".format(idx, idx + len(find_str)-1))
        new_str = data_str.replace(find_str, mask_str, count)
        print(new_str)
        count += 1
    else:
        break
# 찾은 문자열 변경하기