# abstract base class
# 사용 : 각각의 자손클래스에서 다른 내용으로 구현될 것을 예상하고 가이드 라인만 만든다.

from abc import *
from operator import methodcaller

class StudentBase(metaclass=ABCMeta):
    @ abstractmethod
    # tell interpreter "study method is abc so check!"
    def study(self):
        pass
    @abstractmethod
    def go_to_school(self):
        pass

class Student(StudentBase):
    def study(self):
        print("study")
        
class Student1(Student):
    def go_to_school(self):
        print("go to school")
        
if __name__ == "__main__":
    student = Student1()
    student.study()
    student.go_to_school()