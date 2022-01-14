class Circle:
    PI = 3.14

    def __init__(self, radius):
        self.__radius = radius

    def area(self):
        PI = 3.14
        return pow(self.__radius, 2) * PI


c1 = Circle(2)

print("원의 면적: {}".format(c1.area()))
