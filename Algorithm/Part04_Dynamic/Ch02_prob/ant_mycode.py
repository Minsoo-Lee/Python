# 각 식량창고에는 정해진 수의 식량이 저장되어 있음
# 개미 전사는 식량창고를 선택적으로 약탈하여 식량을 뻇음
# 메뚜기 정찰병들은 일직선상에 존재하는 식량창고 중에서 
# 서로 인접한 식량창고가 공격받으면 바로 알아챌 수 있음
# 개미 전사가 정찰병에게 들키지 않고 식량창고를 약탈하기 위해서는
# 최소한 한 칸 이상 떨어진 식량창고를 약탈해야 한다.

# 실패

n = int(input())
food = list(map(int, input().split()))
is_ant = [0] * n

def get_food(x):
    is_ant[x] = 1
    if (x + 2 < n):
        for i in range(x + 2, n):
            get_food(i)
            