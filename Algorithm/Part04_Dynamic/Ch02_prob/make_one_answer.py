# a(i) : i를 1로 만들기 위한 최소 연산 횟수
# 점화식 : a(i) = min[a(i - 1), a(i / 2), a(i / 3), a(i / 5)] + 1
# 단, 1을 빼는 연산을 제외하고는 해당 수로 나누어 떨어질 때에 한해 점화식 사용 가능

# bottom-up
x = int(input())
d = [0] * 30001

for i in range(2, x + 1):
    d[i] = d[i - 1] + 1
    if i % 2 == 0:
        d[i] = min(d[i], d[i // 2] + 1)
    if i % 3 == 0:
        d[i] = min(d[i], d[i // 3] + 1)
    if i % 5 == 0:
        d[i] = min(d[i], d[i // 5] + 1)

print(d[x])