# 입력받은 문자열을 거꾸로 출력
str = input("str : ")
res = ""
for ch in str:
    res = ch + res
print(res)

# list()
s_list = list(str)
print(type(s_list))

# list() 역순
s_list.reverse()
print("".join(s_list))

# reversed 는 문자열 역순
print("".join(reversed(str)))

# 인덱싱으로 역순
print(str[::-1])
print(str[3::-1])