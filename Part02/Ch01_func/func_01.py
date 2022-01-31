
import hello

hello.say_hello("이민수")
hello.say_hello("홍길동")

from hello import *

say_hello("이민수")
say_hello("홍길동")

def get_sum(start, end):
    sum = 0
    for i in range (start, end + 1):
        sum += i
    return sum

result = get_sum(1, 10)
print(type(result))
print(result)