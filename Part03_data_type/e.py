# 자동 판매기를 시뮬레이션하는 프로그램을 작성하는데 사용자는 1000원짜리 지폐와
# 500원, 100원짜리 동전을 사용할 수가 있다. 물건값을 사용자로부터 입력을 받아서
# 1000원권 지폐, 500원 동전, 100원 동전의 개수를 입력하면 거스름돈을 계산하여
# 동전으로 반환하는 프로그램

item_price = int(input("물건값을 입력하세요 : "));
bill_1000 = int(input("1000원 지폐 개수 입력 : "));
coin_500 = int(input("500원짜리 동전 개수 임력 : "));
coin_100 = int(input("100원짜리 동전 개수 입력 : "));

# 거스름돈 구하기
change = ((bill_1000 * 1000) + (coin_500 * 500) + (coin_100 * 100)) - item_price;
print("거스름돈 :", change);

# 거스름돈 500원 개수 계산
nod_500 = change // 500;
change = change % 500;
# 거스름돈 100원 개수 계산
nod_100 = change // 100;
change = change % 100;
# 거스름돈 50원 개수 계산
nod_50 = change // 50;
change = change % 50;
# 거스름돈 10원 개수 계산
nod_10 = change // 10;
change = change % 10;
# 거스름돈 100원 개수 계산
nod_1 = change;
print("500원 : ", nod_500);
print("100원 : ", nod_100);
print("50원 : ", nod_50);
print("10원 : ", nod_10);
print("1원 : ", nod_1);