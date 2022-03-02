# a(i) : 금액 i를 만들 수 있는 최소한의 화폐 개수
# k = 각 화폐의 단위
# 점화식 : 각 화폐 단위인 k를 하나씩 확인하며
# 1. a(i - k)를 만드는 방법이 존재하는 경우 : a(i) = min[a(i), a(i-k) + 1]
# 2. a(i - k)를 만드는 방법이 존재하지 않는 경우 : a(i) = INF

n, m = map(int, input().split())

array = []
for i in range(n):
    array.append(int(input()))
    
d = [10001] * (m + 1)

d[0] = 0
for i in range(n):
    for j in range(array[i], m + 1):
        if d[j - array[i]] != 10001:
            d[j] = min(d[j], d[j - array[i]] + 1)
            
if d[m] == 10001:
    print(-1)
else:
    print(d[m])