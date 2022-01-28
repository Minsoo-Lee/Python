# 문자열 연결
first_name = "Minsoo"
last_name = "Lee"
name = last_name + first_name
print(name)

# 문자열을 숫자로 변환
price = int("123456")
print(type(price))
print(price)

price = float("123456.187")
print(type(price))
print(price)

# 문자열의 반복
# * 연산자를 이용해서 반복
arrow = "->" * 10
print(arrow)
arrow = "->"
print(arrow * 10)

# %s(형식 지정자)
# %s는 문자열이나 숫자값을 변수에 대입해서 자주 변경이 있을 경우 이런 형식을 지정하여
# 상황에 맞게끔 출력을 하도록 한다.
price = 1000        # %s에 정수를 대입
print("가격 : %s" % price)
time = "13:49"      # %s에 문자열을 대입
print("현재 시간 : %s" % time)
# %s를 2개 이상을 사용하ㅣ고자 할 때는 괄호로 묶어준다.
temp = "현재 시간은 %s시 %s분 %s초 입니다."
print(temp % (10, 38, 12))