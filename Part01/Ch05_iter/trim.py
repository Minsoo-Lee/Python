# 왼쪽 공백 제거
str = "     HI!"
print("before :" + str)
print("after :" + str.lstrip())

# 오른쪽 공백 제거
str = "HI!     "
print("before :" + str)
print("after :" + str.rstrip())

# 양쪽 공백 제거
str = "     HI!     "
print("before :" + str)
print("after :" + str.strip())

# 문자열 나누기
str = "I study Python hard"
print(str.split())