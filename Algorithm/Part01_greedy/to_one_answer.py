# 어떠한 수 N이 1이 될 때까지 두 과정중 하나를 반복한다.
# 단, 두 번째 연산은 N이 K로 나누어 떨어질 때만 선택할 수 있다.
# 1. N에서 1을 뺀다.
# 2. N을 K로 나눈다.
# 과정을 수행해야 하는 최소 횟수는?

n, k = map(int, input().split())
res = 0

while True:
    # N이 K로 나누어 떨어지는 수가 될 때까지 빼기
    target = (n // k) * k
    res += (n - target)
    n = target
    # N이 K보다 작을 때(더 이상 나눌 수 없을 때) 반복문 탈출
    if n < k:
        break
    res += 1
    # k로 나누기
    n //= k
    
# 마지막으로 남은 수에 대하여 1씩 빼기
res += (n - 1)
print(res)