# 효율적인 화폐 구성
# N가지 종류의 화폐가 있다.
# 이 화폐들의 개수를 최소한으로 이용해서
# 그 가치의 합이 M원이 되도록 하려고 한다.
# M원을 만들기 위한 최소한의 화폐 개수를 출력하는 프로그램을 작성하시오

# 다이나믹 쓰는게 너무 서투름...

n, m = map(int, input().split())
money = []
for i in range(0, n):
    x = int(input())
    money.append(x)
    
money.reverse()

def get_money():
    my_money = 0
    count = 1
    for i in money:
        if i < m:
            my_money = i
            break
    if my_money == 0:
        return -1
    while my_money != m:
        check = 0
        for i in money:
            if my_money + i <= m:
                my_money += i
                check = 1
                count += 1
                break
        if check == 0:
            return -1
    return count

print(get_money())