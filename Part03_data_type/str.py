# 문자열 실습

# 큰따옴표(double quotation)로 묶으면 문자열이 된다. (권장)
welcome = "Happy New Year 2021"
print(welcome);
print(type(welcome));

# 작은따옴표(single quotation)로 묶어도 문자열이 된다.
welcome = 'Happy New Year 2021';
print(welcome);
print(type(welcome));

# 이스케이프 문자들의 기능을 제거하기 위해 문자열 시작 앞에 r을 붙인다.
message = r"c:\temp\name\a.mp3"
print(message);

# 문자열(영어, 한글 상관X)의 길이를 알고자 한다면 len() 함수를 사용한다.
message = "이민수"
print("문자열의 길이 :", len(message));