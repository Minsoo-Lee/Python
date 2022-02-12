class Circle:
    def __init__(self, radius = 0):
        self.radius = radius
    def __eq__(self, other):
        print("__eq__() called")
        return self.radius == other.radius
    
class Vector:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    # 인스턴스의 더하기 연산을 하고 그에 해당하는 값으로
    # 새로운 인스턴스를 생성하여 리턴해줌
    def __add__(self, other):
        return Vector(self.x + other.x, self.y + other.y)
    def __sub__(self, other):
        return Vector(self.x - other.x, self.y - other.y)
    def __mul__(self, other):
        return Vector(self.x * other.x, self.y * other.y)
    def __str__(self):
        return "(%g %g)" % (self.x, self.y)

if __name__ == "__main__":
    circle1 = Circle(10)
    circle2 = Circle(10)
    # 주소값끼리의 연산은 불가능하지만 __eq__ 덕분에 비교가 가능해짐
    # == 연산자가 __eq__ 함수를 호출
    if circle1 == circle2:
        print("SAME")
    vector1 = Vector(5, 2)
    vector2 = Vector(5, 3)
    print(vector1 + vector2)
    print(vector1 - vector2)
    print(vector1 * vector2)