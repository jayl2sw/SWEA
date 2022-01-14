class Rectangle:
    def __init__(self, height, width):
        self.__height = height
        self.__width = width

    def area(self):
        return self.__height * self.__width


r1 = Rectangle(2, 10)


print("사각형의 면적: {}".format(r1.area()))