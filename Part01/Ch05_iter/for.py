print("안녕하세요")
print("안녕하세요")
print("안녕하세요")
print("안녕하세요")
print("안녕하세요")
print("---------")
for x in [0, 1, 2, 3, 4]:
    print("안녕하세요")
print("---------")
for x in range(5):
    print("안녕하세요")
print(type(range(5)))

# 문자열 리스트를 시퀀스로
s = ["이민수", "김연아", "김철수", "홍길동", "김남길"]
for name in s:
    print("HI", name)
    
# 줄바꿈을 하지 않게 하는 end 인자값
for x in [0, 1, 2, 3, 4]:
    print(x, end = " ")
    
# 알파벳인지 확인
str = "aeiousc123"
for ch in str:
    if ch.isalpha():
        print(ch)