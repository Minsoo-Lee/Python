# anonymous function : No function name
# make func "lambda" keyword
# cannot call

from tkinter import Y


x = 150

def main():
    print("sum :", get_sum(10, 50))
    print("sum :", get_sum(100, 50))
    print("lambda sum :", sum(10, 50))
    print("lambda sum :", sum(100, 50))
    print("lambda sum :", sum(x, 50))
    print("lambda sum :", sum(x, 50))
    # call directly
    print((lambda x, y : x + y)(10, 50))

# general function    
def get_sum(x, y):
    return x + y

# lambda keyword
# usually using in calllback function taking events
# cannot allocate value in variable
# lambda x=10, y : x + y => NO!
sum = lambda x, y : x + y

li = [lambda x : x ** 2, lambda x : x ** 3, lambda x : x ** 4]

for i in li:
    print(i(10))

main()