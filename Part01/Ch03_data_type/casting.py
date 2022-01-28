from math import *

# 지구에서 가장 가까운 별은 프록시마 켄타우리
# 프록시마 켄타우리는 지구로부터 40 * 10^12 km 떨어져 있음
# 빛의 속도로 이 별에 간다면 시간이 얼마나 걸리는지 계산하는 프로그램
# 빛의 속도 : 초당 30만 km

light_speed = 300000
distance = 40 * pow(10, 12);
print(distance);

sec = distance / light_speed;
print("걸리는 시간(초) :", sec);

# 정수 - 실수 계산은 결과값이 실수로 나옴
light_year = sec / (60 * 60 * 24 * 365);
print("걸리는 년도 :", light_year);

# 정수 10과 실수 10.0은 동일하다.
print(10 == 10.0);
# 문자열 10과 실수 10.0은 완전히 다른 것으로 인식
print("10" == 10.0);