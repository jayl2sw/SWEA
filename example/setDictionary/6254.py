dictionary ={ '홍길동' : '010-1111-1111',
              '이순신' : '010-1111-2222',
              '강감찬' : "010-1111-3333"}
            



print("아래 학생들의 전화번호를 조회할 수 있습니다.")
for i in range(3):
    print(dictionary['name'])

n = input("전화번호를 조회하고자 하는 학생의 이름을 입력하십시오.")

print(f'{n}의 전화번호는 {dictionary[f"{n}"]}입니다.')