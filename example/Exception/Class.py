# SyntaxError = 구문 오류
# 예외 = 문법적인 문제는 없는데 실행 중에 예기치 않게 발생 (프로그램이 끝날 수 있다.)
# IndexError
'''
data_list = [10, 20, 30]
print(data_list[3])
'''

# ValueError 숫자 대신 str이 들어감

# if문을 이용한 예외의 처리--> 정상적인 흐름을 제어할 경우에만 사용

# try~except 이용
'''
print("사각형의 면적을 구해봅시다.")

width = input("폭을 입력하세요: ")
height = input("높이를 입력하세요: ")
area = 0

if width.isdigit() and height.isdigit():    # 숫자문자의 경우 TRUE 반환
    area = int(width) * int(height)
    print("{} x {} = {}".format(width,height, area))
else:
    print("숫자가 아닌 문자가 입력되었습니다.")
'''
'''
try ~ except : 예외가 발생했을 때 처리
try ~ except ~ else : 예외가 발생했을 때, 예외가 발생하지 않았을 때 
try ~ except ~ else ~ finally: 예외가 발생했을 때, 예외가 발생하지 않았을 때 + 둘 다 실행
'''

# print("사각형의 면적을 구해봅시다.")
#
# width = input("폭을 입력하세요: ")
# height = input("높이를 입력하세요: ")
# area = 0
#
# try:
#     area = int(width) * int(height)
#
# except:
#     print("숫자가 아닌 문자가 입력되었습니다.")
# else:
#     print("{} x {} = {}".format(width, height, area))
#
# finally:
#     print("finally 코드 블록은 예외 발생 여부에 상관없이 실행됩니다.")
#     print("프로그램을 종료합니다...")

# 예외 객체 --> 코드 실행 중 오류가 발생하면 만들어진 것

# print("사각형의 면적을 구해봅시다.")
#
# width = input("폭을 입력하세요: ")
# height = input("높이를 입력하세요: ")
# area = 0
#
# try:
#     area = int(width) * int(height)
#
# except Exception as ex:
#     print("{}: {}".format(type(ex),ex))
# else:
#     print("{} x {} = {}".format(width, height, area))
#
# finally:
#     print("finally 코드 블록은 예외 발생 여부에 상관없이 실행됩니다.")
#     print("프로그램을 종료합니다...")

# print("나누기 연산의 결과를 구해봅시다.")
#
# x, y, result = 0,0,0
#
# try:
#     x = int(input("피제수를 입력하세요: "))
#     y = int(input("제수를 입력하세요: "))
#     result = x / y
# except ValueError as ve:
#     print("입력값은 반드시 숫자를 사용해야 합니다.")
#     print("{}: {}".format(type(ve), ve))
# except ZeroDivisionError as ze:
#     print("제수로 0을 사용 할 수 없습니다.")
#     print("{}: {}".format(type(ze),ze))
#
# else:
#     print("{} / {} = {}".format(x, y, result))
# finally:
#     print("finally 코드 블록은 예외 발생 여부에 상관없이 실행됩니다.")
#
# print("프로그램이 종료됩니다.")

# 강제 예외 발생 (특정 조건에서 예외 객체를 만들어 예외를 일으킬 수 있음)
#
# def calc_area(w,h):
#     if w.isdigit() and h.isdigit():
#         return int(w) * int(h)
#     else:
#         raise ValueError("숫자가 아닌 값이 입력되었습니다.")
#
# print("사각형의 면적을 구해봅시다.")
#
# width = input("폭 입력: ")
# height = input("높이 입력: ")
#
# try:
#     area = calc_area(width, height)
# except ValueError as ve:
#     print("{}: {}".format(type(ve), ve))
# except Exception as ex:
#     print("{}: {}".format(type(ex), ex))
# else:
#     print("{} x {} = {}".format(width,height,area))
# finally:
#     print("finally 코드 블록은 예외 발생 여부에 상관없이 실행됩니다.")
# print("프로그램을 종료합니다.")

# 10-11.py

def input_index():
    num = 0
    try:
        num = int(input("인덱스로 사용할 숫자를 입력하세요: "))
    except ValueError as exception:
        raise exception
    else:
        return num

data_list = list(range(1, 11))

def print_in_bounds(list, index):
    value = 0
    try:
        value = list[index]
    except IndexError as exception:
        print("{}: {}".format(type(exception), exception))
        index = len(list) - 1
        print("인텍스는 0 ~ {}까지 사용할 수 있습니다.".format(index))
        value = list[index]
    finally:
        print("[{}]: {}".format(index,value))


print("data_list: {0}".format(data_list))

try:
    num = input_index()
    print_in_bounds(data_list, num)
except ValueError as ve:
    print("{0}: {1}".format(type(ve), ve))
except Exception as exception:
    print("{}: {}".format(type(exception), exception))

