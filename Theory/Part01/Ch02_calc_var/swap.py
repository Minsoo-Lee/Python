num1 = 100;
num2 = 200;

# 데이터 타입 확인을 위해서는 type 함수를 사용하면 된다.
print(type(num1));

print("num1 : ", num1, " / num2 : ", num2);
num1, num2 = num2, num1;
print("num1 : ", num1, " / num2 : ", num2);