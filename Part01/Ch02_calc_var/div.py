myMoney = 5000;
candyPrice = 120;

# 최대로 살 수 있는 사탕의 개수 (실수값)
numCandies = myMoney / candyPrice;
print("최대로 살 수 있는 사탕의 개수(실수값): ", numCandies);

# 최대로 살 수 있는 사탕의 개수 (정수값)
numCandies = myMoney // candyPrice;
print("최대로 살 수 있는 사탕의 개수(정수값) : ", numCandies);

# 최대로 살 수 있는 사탕을 구입하고 남은 돈
change = myMoney % candyPrice;
print("최대로 살 수 있는 사탕을 구입하고 남은 돈 : ", change);