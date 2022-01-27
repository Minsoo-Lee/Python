# 변수 temp에 10 저장
temp = 10;
# 괄호 없어도 상관 X
if (temp > 20) :
    print("얇은 옷을 입으세요!");
else :
    print("두꺼운 옷을 입으세요!");
print("\n");

# 숫자 맞추기
print("숫자게임을 시작합니다.");
number = 62;
# input()은 사용자로부터 값을 입력받기 위해서 사용된다.
exact_num = input("1에서 100 사이의 수를 추측해보세요");
print(exact_num);
# 문자열로 넘어온 값을 int()를 이용하여 숫자로 바꿈
guess = int(exact_num);
if (guess == number) :
    print("맞았습니다.");
else : 
    print("틀렸습니다.");
print("게임이 끝났습니다.");