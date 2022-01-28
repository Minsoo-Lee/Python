# int
print(type(17));
# float
print(type(10.77));
# str
print(type("HI!"));

# volume of sphere / radius r
from math import *
r = 5.0;
v = 4.0 / 3.0 * pi * pow(r, 3);
print("구의 부피 : ", v);
# 문자열 + float 은 타입 일치가 되지 않아 문자열을 생성할 수 없음
# print("구의 부피 : " + float) 오류!
print("구의 부피 : " + str(v));

# area
a = 4 * pi * pow(r, 2);
print("구의 겉넓이 : ", a);