# 모든 클래스의 최고 조상클래스는 object 클래스
# parent
class Phone(object):
    def __init__(self):
        self.model = ""
        self.color = ""
    def power_on(self):
        print("turn on")
    def power_off(self):
        print("turn off")
    def bell(self):
        print("bell ring")

# child
class Dmb(Phone):
    def __init__(self, model, color, channel):
        super().__init__()
        self.model = model
        self.color = color
        self.channel = channel
    def power_on_dmb(self):
        print("turn on:", self.channel)

if __name__ == "__main__":
    dmb = Dmb("Python", "black", 10)
    print("model:", dmb.model)
    print("color:", dmb.color)
    print("channel:", dmb.channel)
    
    dmb.power_on()
    dmb.bell()
    dmb.power_on_dmb()