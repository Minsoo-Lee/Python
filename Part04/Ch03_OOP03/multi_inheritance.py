class Person(object):
    def __init__(self):
        pass
    def greeting(self):
        print("HI")

class Univ(object):
    def __init__(self):
        pass
    def credit(self):
        print("mange credit")

class Student(Person, Univ):
    def __init__(self):
        Person.__init__(self)
    def study(self):
        print("study")
        
if __name__ == "__main__":
    student = Student()
    student.greeting()
    student.credit()
    student.study()