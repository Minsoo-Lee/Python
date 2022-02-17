# 어떠한 수 N이 1이 될 때까지 두 과정중 하나를 반복한다.
# 단, 두 번째 연산은 N이 K로 나누어 떨어질 때만 선택할 수 있다.
# 1. N에서 1을 뺀다.
# 2. N을 K로 나눈다.
# 과정을 수행해야 하는 최소 횟수는?

count = 0
n, k = map(int, input().split())
while (True):
    if (n % k == 0 and (n // k) < (n - 1)):
        n //= k
    else:
        n -= 1
    count += 1
    if n == 1:
        break;
print(count)