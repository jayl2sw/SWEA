class Person:
    def __init__(self):
        pass

    def getGender(self):
        return "Unknown"

class Male(Person):
    def __init__(self):
        self.__gender = "Male"

    def getGender(self):
        Person.getGender(self)
        return self.__gender

class Female(Person):
    def __init__(self):
        self.__gender = "Female"

    def getGender(self):
        Person.getGender(self)
        return self.__gender

p1 = Male()
p2 = Female()

print(p1.getGender())
print(p2.getGender())