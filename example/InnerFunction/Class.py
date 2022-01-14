# 수칙연산 관련
val1 = 10
val2 = 4
'''
abs(val1)           # 절대값 반환
divmod(val1, val2)   # 몫과 나머지 반환
pow(val1, val2)      # val1^val2 반환

# 시퀀스형, 반복가능 자료형
all()       # 모두 True 일 때, True 반환
any()       # 모두 False 일 때, False 반환 None ==> False
enumerate() #
'''


#
# data_list = [10, 20, 30, 40, 50]
# print(enumerate(data_list))
# for idx, val in enumerate(data_list):
#     print("data_list{}: {}".format(idx, val))
#
# print("-"*25)
#
# for obj in enumerate(data_list):
#     print("{}: {}, {}".format(type(obj), obj[0], obj[1]))
#
# print("-"*25)
#
# for obj in enumerate(data_list):
#     print("{0}: {1}, {2}".format(type(obj), *obj))
#

# filter() # 조건에 해당하는 항목을 걸러내는 함수
# 첫번째 매개변수 True or False
# 두번째 매개변수 자료형 인자
'''
def iseven(num):
    return num % 2 == 0


numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

ret_val = filter(iseven, numbers)
ret_val = filter(lambda n: n%2==0, numbers)
print(type(ret_val))
print(list(ret_val))
'''
# set() --> 순서 무의미, 중복 허용하지 않음
# dict, enumerate 딕셔너리 만듬
# map()
# max() 가장 큰 값 반환
# min() 가장 작은 값 반환
# range(시작값, 종료값, 증가값)
# sorted() 오름차순 , reversed 내립차순
# zip() 둘이상의 반복 가능한 자료형을 인자로 전달받아, 동일 위치의 항목을 묶어 튜플을 항목으로 구성하는 zip객체를 생성하는 함수
# zip() example
'''
data_list1 = [1,2,3]
data_list2 = [4,5,6]
data_list3 = ["a", "b", "c"]

print(list(zip(data_list1,data_list2,data_list3)))
'''
# 변환함수
# chr() 정수형태의 유니코드 --> 문자
# ord() 문자 --> 유니코드 값 (10진 정수형태)
# hex() 10진 정수 --> 16진 정수

# print(chr(65), chr(97), chr(0xac00))
# print(ord("A"), ord("a"), ord("가"))
# print(hex(ord("가")))

# int()     숫자형식의 문자열 --> 정수
# float()   인자 --> 소수
# str()     인자 --> 문자열
#
# x = "10"
# y = "3C"
# z = 4.5
#
# print(int(x,2), int(y,16), int(z), int(x), str(z))

# 객체 조사를 위한 함수
# dir() 인자로 전달된 객체가 가지고 있는 변수, 메서드와 같은 속성 정보를 리스트 객체로 반환

# print(dir())
# str = "Hello, Python"
# print(dir(str))
# data_list= [10,20,30,40,50]
# print(dir(data_list))

#globals() # 현재의 전역 심볼 테이블을 보여주는 딕셔너리를 반환하는 함수 # 전역변수와 함수, 클래스의 정보 포함
#locals()  #현재 지역 심볼 테이블을 보여주는 딕셔너리를 반환
'''
class MyClass:
    pass

def test_fn(param):
    def inner_fn():
        pass
    val1 = 5
    val2 = 8
    for item in locals().items():
        print("\t{}:{}".format(item[0],item[1]))

val1 = 10
val2 = 20
obj1 = MyClass()

g = dict(globals())

print("globals()")
for item in g.items():
    print("\t{}:{}".format(item[0],item[1]))

print("\n\nlocals()")
test_fn(10)
'''

# id() 인자로 전달된 객체의 고유 주소(참조값)을 반환하는 함수
"""
x = 10
print("{} x의주소값: {}".format(type(x), hex(id(x))))
y = 10
print("{} x의주소값: {}".format(type(y), hex(id(y))))
z = '10'
print("{} x의주소값: {}".format(type(z), hex(id(z))))
"""

# isinstance() 첫번째 인자로 전달 된 객체가 두번째 인자로 전달된 클래스의 인스턴스인지에 대한 여부를 반환
# issubclass() 첫번째 인자로 전달 된 클래스가 두번째 인자로 전달된 클래스의 서브 클래스인지에 대한 여부를 반환
'''
class Parent:
    pass

class Child(Parent):
    pass

p = Parent()
c = Child()

print(isinstance(p,Parent))
print(isinstance(c,Parent))
print(isinstance(p,Child))
print(isinstance(c,Child))
print(issubclass(Child, Parent))
'''

# 실행관련함수
# eval() 실행가능한 표현식의 문자열을 인자로 전달받아 해당 문자열의 표현식을 실행한 결과값을 반환하는 함수

# 09-21.py

data_list = list(range(1,21))

print("data_list: {0}".format(data_list))

map_str = input("항목 x에 대해 적용할 표현식을 입력하세요: ")

map_list = list(map(lambda x: eval(map_str), data_list))

print("data_list에 대한 map 함수의 적용 결과: {}".format(map_list))

filter_str = input("항목 x에 대해 필터링할 조건의 표현식을 입력하세요: ")

filter_list = list(filter(lambda x: eval(filter_str), map_list))

print("map_list에 대해 filter 함수의 적용 결과: {}".format(filter_list))