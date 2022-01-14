class Student:
    def __init__(self, name):
        self.__name = name

    @property
    def name(self):
        return self.__name

class GraduateStudent(Student):
    def __init__(self, major, st_name):
        Student.__init__(self, st_name)
        # super().__init__(st_name)
        self.__major = major

    @property
    def major(self):
        return self.__major


s1 = Student("홍길동")
s2 = GraduateStudent("컴퓨터", "이순신")

print("이름: {}".format(s1.name))
print("이름: {}, 전공: {}".format(s2.name, s2.major))