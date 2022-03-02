# 모험가 길드에서는 N명의 모험가를 대상으로 '공포도'를 측정했는데,
# '공포도'가 높은 모험가는 쉽게 공포를 느껴 위험 상황에서 제대로 대처할 능력이 떨어진다.
# 공포도가 X인 모험가는 반드시 X명 이상으로 구성한 모험가 그룹에 참가해야 한다.
# N명의 모험가에 대한 정보가 주어졌을 때, 여행을 떠날 수 있는 그룹 수의 최댓값을 구하시오.
# ex. N = 5, 공포도 = [2, 3, 1, 2, 2]
# => 그룸 1에 공포도가 1, 2, 3 + 그룹 2에 공포도가 2인 두 명

n = int(input())
lst = sorted(list(map(int, input().split())))
people = 0
count = 0

while people < len(lst):
    scare = lst[people]
    people += scare
    if (people >= len(lst)):
        break
    count += 1

print(count)