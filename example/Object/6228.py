class Shape:
    def __init__(self):
        pass

    def area(self):
        return 0


class Square(Shape):
    def __init__(self, length):
        self.__length = length

    def area(self):
        Shape.area(self)
        # super().area()
        return self.__length * self.__length



s1 = Square(3)
print("정사각형의 면적: {}".format(s1.area()))