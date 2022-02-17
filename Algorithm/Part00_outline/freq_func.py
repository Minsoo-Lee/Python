# 1. sum()
result = sum([1, 2, 3, 4, 5])
print(result)

# 2. min(), max()
min = min(7, 3, 5, 2)
max = max(7, 3, 5, 2)
print(min, max)

# 3. eval() : string->formula
result = eval("(3+5)*7")
print(result)

# 4. sorted()
result = sorted([0, 1, 8, 5, 4])
rev_res = sorted([0, 1, 8, 5, 4], reverse=True)
print(result)
print(rev_res)

# 5. sorted() + key
array = [('gildong', 35), ('soonsin', 75), ('minsoo', 50)]
res = sorted(array, key=lambda x:x[1], reverse=True)
print(res);

# 6. permutations
from itertools import permutations
data = ['A', 'B', 'C']
res = list(permutations(data, 3))
print(res)

# 7. combinations
from itertools import combinations
res = list(combinations(data, 2))
print(res)

# 8. product(중복 순열)
from itertools import product
res = list(product(data, repeat=2)) # 2개를 뽑는 모든 순열 구하기(중복 허용)
print(res)

# 9. combinations_with_replacement(중복 조합)
from itertools import combinations_with_replacement
res = list(combinations_with_replacement(data, 2))
print(res)

# counter : 각 원소의 등장 횟수를 세는 기능
from collections import Counter
counter = Counter(['red', 'blue', 'red', 'green', 'blue', 'blue'])
print(counter['blue']) # blue 등장 횟수 출력
print(counter['green']) # green 등장 횟수 출력
print(dict(counter)) # 사전 자료형으로 반환

# gcd, lcm(최대공약수, 최소공배수)
import math
def lcm(a, b):
    return a*b // math.gcd(a, b)
a = 21
b = 14
print(math.gcd(a, b))
print(lcm(a, b))