class Korean:
    def __init__(self):
        self.__nationality = "대한민국"

    def printNationality(self):
        return print("{}".format(self.__nationality))

s1 = Korean()
s2 = Korean()

s1.printNationality()
s2.printNationality()