class Rectangle:
    def __init__(self, side = 0):
        self.side = side
    def get_area(self):
        return self.side * self.side
    
def print_area(rectangle, cnt):
    print("length \t area")
    while cnt >= 1:
        print(rectangle.side, "\t", rectangle.get_area())
        rectangle.side += 1
        cnt -= 1

if __name__ == "__main__":
    rectangle = Rectangle()
    cnt = 5
    print_area(rectangle, cnt)
    print("length:", rectangle.side);