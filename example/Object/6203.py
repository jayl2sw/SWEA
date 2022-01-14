class score:
    def __init__(self, korean, english, math):
        self.__korean = korean
        self.__english = english
        self.__math = math

    def sum(self):
        return self.__korean + self.__math + self.__english


l, m, n = map(int, input().split(','))


s1 = score(l, n, m)
print("국어, 영어, 수학의 총점: {}".format(s1.sum()))
