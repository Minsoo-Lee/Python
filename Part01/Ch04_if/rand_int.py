from random import *

# randint(a, b) : a <= x <= b
num = randint(1, 6)
print("dice :", num)

# random : 0.0 <= x < 1.0 (float)
num = random()
print("num :", num)

# randrange(a, b, c) : a <= x <= b, c 간격
num = randrange(1, 101, 2)
print("num :", num)

# randrange(a) : 0 <= x < a
num = randrange(10)
print("num :", num)