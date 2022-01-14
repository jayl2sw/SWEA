# 객체 = 변수(값) + 메서드(실행코드, 변수와 연관된 기능)
# ex) 자동차 - 연료량, 속도계 + 주행
# 객체 --> 부품화, 재사용성
# 설계도 - 클래스 (부품 객체를 만들기 위한 청사진)
# 자동차 클래스
# 클래스 + 객체 + 메서드
# 객체 - 메모리에 로딩된 클래스를 통해 클래스를 템플릿으로 하여 메모리 상에 생성된 정보 --> 인스턴스
# 자신 고유의 속성을 가지며 클래스에서 정의한 행위 수행
# 메서드 - 메시지, 클래스로부터 생성된 객체 사용 시 객체에 명령을 내리는 행위
# 객체의 속성을 조작할 목정으로 사용

# 객체지향 프로그램의 특징
# 추상화 - 객체에서 공통된 속성과 행위를 추출
# 데이터 타입의 표현과 연산을 캡슐화 --> 접근 제어를 통해 정보 은닉
# 추상 데이터 타입 - 클래스, 인스턴스 - 객체, 연산 - 메서드
# 상위 클래스 --> 하위 클래스, 하위 클래스에서 속성과 행위 사용 가능
# 부모 - 자식, 기반 - 파생, 상위 - 하위, 슈퍼 - 서브
# 재사용으로 인해 코드가 줄어듦, 범용적인 사용 가능 object --> string or int 상관없음
# 자료와 메서드의 자유로운 사용 및 추가 가능
# 다형성 - 다양한 형태로 나타날 수 있는 특징
# 클래스 - 행위 여러개, 상위 클래스의 행위 --> 하위 클래스의 행위
# 어떤 한 요소에 여러 개념을 넣어 놓는 것,
# 같은 이름의 메서드가 여러 클래스에서 다른, 인자에따라 다른 역할
# 메서드 오버로딩 - 클래스 내부에 동일한 이름의 행위를 여러개 정의 하는 것
# 이름 같고, 변수의 타입과 수 서로 다름, 리턴 타입 관계 x

# 특정그룹 이름과 나이 관리
# 딕셔너리 객체 필요, --> 리스트 객체의 항목으로 사용

# members = [
#     {"name": "홍길동", "age": 20},
#     {"name": "이순신", "age": 45},
#     {"name": "강감찬", "age": 35}
# ]

# for member in members:
#     print("{}\t{}".format(member["name"],member["age"]))

# 딕셔너리 객체 -> 한명의 멤버 정보만 다룸
# 여러개 만듬

# --------------------------------------------------------------------------------

# def create(name, age):
#     return {"name": name, "age": age}
#
# def to_str(person):
#     return "{}\t{}".format(person["name"], person["age"])
#
# members = [
#     create("홍길동", 20),
#     create("이순신", 45),
#     create("강감찬", 35)
# ]
#
# for member in members:
#     print(to_str(member))

# --------------------------------------------------------------------------------

# 멤버 클래스 설계 --> 제작 --> 객체

# class Person:
#     def __init__(self, name, age): # self = 생성된 객체 공간을 가리키는 식별자
#         self.__name = name
#         self.__age = age      # 캡슐화 된 필드로 만드는 것이 필요 할 수 있음. // 입력 시 유효성 검사를 할 수 없음.
#                             # 너무 높은 값 or 음수 // 검증을 위해 적절한 멤버 필드의 접근이 필요
#                             # 외부에서 필드에 접근하는 것 제한
#         print("{} 객체가 생성되었습니다.".format(self.name))
#
#     def __del__(self):
#         print("{} 객체가 제거되었습니다.".format(self.name))
#
#     def to_str(self):
#         return "{}\t{}".format(self.__name,self.__age)
#
#     def get_name(self):
#         return self.__name
#
#     def get_age(self):
#         return self.__age
#
#     def set_age(self, age):
#         if age < 0:
#             raise TypeError("나이는 0이상의 값만 허용합니다.")
#         self.__age = age
#
# members = [
#     Person("홍길동", 20),
#     Person("이순신", 45),
#     Person("강감찬", 35)
# ]
#
#
# members[0].set_age(20)
#
# for member in members:
#     print(member.to_str())

# self.변수 형태를 가지는 변수 = 인스턴스 변수
'''
class Person:
    def __init__(self, name, age):
        self.__name = name
        self.__age = age
        print("{} 객체가 생성되었습니다.".format(self.__name))

    def __del__(self):
        print("{} 객체가 제거되었습니다.".format(self.__name))

    def to_str(self):
        return "{}\t{}".format(self.__name, self.__age)

    @property
    def name(self):
        return self.__name

    @property
    def age(self):
        return self.__age

    @age.setter
    def age(self, age):
        if age < 0:
            raise TypeError("나이는 0이상의 값만 허용합니다.")
        self.__age = age

members = [
    Person("홍길동", 20),
    Person("이순신", 45),
    Person("강감찬", 35)
]

members[0].age = 22

for member in members:
    print(member.to_str())
'''

# getter/setter 대신 데코레이터 사용 할 수 있음
# 변수 이름과 같은 메서드 만들어 사용 가능 @property or property.setter

# 클래스 변수 : 클래스 내에서 클래스명.변수 형식으로

# class 클래스명:
#     클래스변수 = 값

# 클래스 변수의 count 활용법
'''
class Person:
    count = 0  # 클래스 변수 count 활용

    def __init__(self, name, age):
        self.__name = name
        self.__age = age
        Person.count += 1
        print("{} 객체가 생성되었습니다.".format(self.__name))

    def __del__(self):
        print("{} 객체가 제거되었습니다.".format(self.__name))

    def to_str(self):
        return "{}\t{}".format(self.__name, self.__age)

    @property
    def name(self):
        return self.__name

    @property
    def age(self):
        return self.__age

    @age.setter
    def age(self, age):
        if age < 0:
            raise TypeError("나이는 0이상의 값만 허용합니다.")
        self.__age = age

    @classmethod
    def get_info(cls):
        return "현재 Person 클래스의 인스턴스는 총 {} 개입니다.".format(cls.count)

    def __gt__(self, other):
        return self.__age > other.__age

    def __lt__(self, other):
        return self.__age < other.__age

    def __ge__(self, other):
        return self.__age >= other.__age

    def __le__(self, other):
        return self.__age <= other.__age

    def __eq__(self, other):
        return self.__age == other.__age

    def __ne__(self, other):
        return self.__age != other.__age

    def __str__(self):
        return "{}/t{}".format(self.__name, self.__age)

members = [
    Person("홍길동", 20),
    Person("이순신", 45),
    Person("강감찬", 35)
]

print(Person.get_info())

members[0].age = 22

for member in members:
    print(str(member))

cnt = len(members)

i = 0

while True:
    print("members[{}] > members[{}] => {}".format(i, i + 1, members[i] > members[i + 1]))
    i += 1
    if i == cnt - 1:
        print("members[{}] > members[{}] => {}".format(i, 0, members[i] > members[0]))
        break
'''
# 클래스 메서드 = 클래스가 소유한 메서드
# @classmethod def클래스매서드(cls, ...)

# 연산자 오버로딩 --> 연산자 --> 각 클래스의 미리 정의된 매서드와 매핑되어 있다.
# 사용자 정의 클래스에서는 연산자를 중복해서 정의 해야 한다 == 연산자 오버로딩
# 비교연산자의 오버로딩 실슴

# __str()__메서드 구현 --> str()함수에 객체를 전달해 문자열로 변환

# 클래스 상속 부모클래스의 동작을 자식클래스에서  재사용, 확장, 수정 단일 상속만 지원!

#class 클래스명(부모클래스명):
class Parent:
    def __init__(self, family_name):
        self.__family_name = family_name
        print("Parent 클래스의 __init__()...")

    @property
    def family_name(self):
        return self.__family_name

    def print_info(self):
        print("Parent: {}".format(self.family_name))

class Child(Parent): #Parent 클래스 상속
    def __init__(self, first_name, last_name):
        Parent.__init__(self, last_name) #매개변수 초기화
        # super().__init__(last_name) #super호출과 생
        self.__first_name = first_name

    @property
    def first_name(self):
        return self.__first_name

    @first_name.setter
    def first_name(self, first_name):
        self.__first_name = first_name

    @property
    def name(self):
        return "{} {}".format(self.family_name, self.first_name)

    def print_info(self):
        Parent.print_info(self)
        # super().print_info()
        print("child: {}".format(self.name))


child = Child("길동", "홍")

print(child.family_name)
print(child.first_name)
print(child.name)
print("========>")

child.first_name = "길순"
print(child.name)


print(child.print_info())
#메서드 오버라이딩 : 상속관계에서 부모클래스에 있는 메서드와 동일한 서명을 가진 메서드를 자식 클래스에서 다시 정의해 사용하는 것



# 15-15.py
"""
class Student:

    def __init__(self, name, gender, height):
        self.__name = name
        self.__gender = gender
        self.__height = height

    @property
    def name(self):
        return self.__name

    @property
    def gender(self):
        return self.__gender

    @property
    def height(self):
        return self.__height

    @height.setter
    def height(self, height):
        self.__height = height

    def __repr__(self):
        return "{0}(name: {1}, gender: {2}, height: {3})" \
            .format(self.__class__.__name__, self.name, self.gender, self.height)


students = [
    Student("홍길동", "남", 176.5),
    Student("이순신", "남", 188.5),
    Student("강감찬", "남", 182.3),
    Student("유관순", "여", 158.4)
]

for student in students:
    print(student)

print("name으로 오름차순 정렬 후 ===> ")
for student in sorted(students, key=lambda x: x.name):
    print(student)

print("name으로 내림차순 정렬 후 ===> ")
for student in sorted(students, key=lambda x: x.name, reverse=True):
    print(student)

print("height으로 오름차순 정렬 후 ===> ")
for student in sorted(students, key=lambda x: x.height):
    print(student)

print("height으로 내림차순 정렬 후 ===> ")
for student in sorted(students, key=lambda x: x.height, reverse=False):
    print(student)

"""