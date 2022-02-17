class Car:
    # field
    color = ""
    speed = 0
    # method
    def up_speed(self, speed):
        # self == this
        self.speed = speed
    def down_speed(self, speed):
        self.speed = speed



if __name__ == "__main__":
    my_car1 = Car()
    my_car2 = Car()
    my_car3 = Car()
    
    my_car1.color = "blue"
    my_car1.speed = 50
    print("%s , %d" % (my_car1.color, my_car1.speed))