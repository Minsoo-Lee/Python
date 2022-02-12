# parent
class Car:
    speed = 0
    door = 0
    def __init__(self, speed, door):
        self.speed = speed
        self.door = door
    def control_speed(self, speed):
        self.speed += speed
        print("parent speed:", self.speed)
        print("parent door:", self.door)
        
# child
class Sedan(Car):
    def __init__(self, speed, door):
        Car.__init__(self, speed, door)
        # 있으나 없으나
        # self.speed = speed
        # self.door = door

if __name__ == "__main__":
    sedan = Sedan(100, 4)
    sedan.control_speed(100)