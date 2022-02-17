# 문자열의 인덱싱
# 파이썬의 특수기능 : 인덱스 처리 시 음수도 사용 가능

word = "Python"
print(len(word))
print(word[0])
print(word[5])
print(word[len(word) - 1])

# 한 번 작성된 문자열은 변경이 불가능하다.
# word[2] = 'B'; // 오류발생

# 사용자로부터 문자열을 3개 입력받음
# 그 후 각 해당 문자열의 첫 번째 문자를 인덱싱하여 문자열로 만든다.
str1 = input("첫 번째 단어를 입력하세요 : ")
str2 = input("두 번째 단어를 입력하세요 : ")
str3 = input("세 번째 단어를 입력하세요 : ")

word = str1[0] + str2[0] + str3[0]
print(word)