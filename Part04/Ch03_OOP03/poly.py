class Animal:
    def __init__(self, name, age, instance):
        self.__name = name
        self.__age = age
        self.__instance = instance
    def show(self):
        print("name:", self.__name)
        print("age:", self.__age)
        self.__instance.sound()
        print("---------------------")
    
class Dog():
    d_name = "dog"
    def sound(self):
        print("meong meong")

class Cat(Animal):
    d_name = "cat"
    def sound(self):
        print("meow meow")
        
if __name__ == "__main__":
    ani1 = Animal("choco", 3, Dog())
    ani1.show()