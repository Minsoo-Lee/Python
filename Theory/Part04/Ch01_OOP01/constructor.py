class Person:
    name = ""
    age = 0;
    height = 0
    weight = 0
    address = ""
    # basic Constuctor
    def __init__(self):
        self.name = "minsoo"
        self.age = 35
        self.height = 175
        self.weight = 70
        self.address = "Seoul"
    # getter()
    def get_name(self):
        return self.name
    def get_age(self):
        return self.age
    def get_height(self):
        return self.height
    def get_weight(self):
        return self.weight
    def get_address(self):
        return self.address
    # setter()
    def set_name(self, name):
        self.name = name
    def set_age(self, age):
        self.age = age
    def set_height(self, height):
        self.height = height
    def set_weight(self, weight):
        self.weight = weight
    def set_address(self, address):
        self.address = address
    # str
    def __str__(self):
        print(self.name)
        print(self.age)
        print(self.height)
        print(self.weight)
        print(self.address)