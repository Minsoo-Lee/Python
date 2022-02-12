# overiding: modify parent's member method

# parent
class Car:
    speed = 0
    def up_speed(self, speed):
        self.speed += speed
        print("speed(parent):", self.speed)
    # __ : private
    def __down_speed(self, speed):
        self.speed -= speed
        print("speed(parent):", self.speed)
    
# child
class Sedan(Car):
    def up_speed(self, speed):
        self.speed += speed
        if self.speed > 150:
            self.speed = 150
            print("can't over 150")
        print("speed(child):", self.speed)
    def down_speed(self, speed):
        self.speed -= speed
        self.__down_speed(100)
        print("speed(child):", self.speed)

class Truck(Car):
    pass

if __name__ == "__main__":
    sedan1 = None
    truck1 = None
    
    sedan1 = Sedan()
    truck1 = Truck()
    print("sedan speed:", end = "")
    sedan1.up_speed(200)
    print("truck speed:", end = "")
    truck1.up_speed(200)
    sedan1.down_speed(120)