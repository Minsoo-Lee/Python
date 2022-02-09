class Monitor:
    price = 0
    color = ""
    # constructor
    def __init__(self, price, color):
        self.price = price
        self.color = color
    def __str__(self):
        print(self.price)
        print(self.color)