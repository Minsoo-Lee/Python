# 피보나치 수열
# 1 1 2 3 5 8 13 21 34 55 89 ...
# a(n) = a(n-1) + a(n-2)

import time

start = time.time()

d = [0] * 100

d[1] = 1
d[2] = 1
n = 99

for i in range(3, n + 1):
    d[i] = d[i - 1] + d[i - 2]

print(d[n])
end = time.time()
print(end - start)