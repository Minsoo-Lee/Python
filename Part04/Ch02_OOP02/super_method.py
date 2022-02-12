class Car:
    value = "field of parent"
    def car_method(self):
        print("parent called")

class Sedan(Car):
    value = "field of child"
    def car_method(self):
        super().car_method()
        print("child called")
        print("parent value:", super().value)
        print("child value:", self.value)

if __name__ == "__main__":
    sedan = Sedan()
    sedan.car_method()