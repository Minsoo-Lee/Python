# deque-list 성능 비교
from collections import deque
import time

# append
# deque
deque_test = deque()
start = time.time()

for i in range(100000000):
    deque_test.append(i)

end = time.time()
print("deque append:", end - start)

# list
lst = list()
start = time.time()

for i in range(100000000):
    lst.append(i)

end = time.time()
print("list append:", end - start)

# pop
# deque
start = time.time()

for i in range(100000000):
    deque_test.pop()

end = time.time()
print("deque pop:", end - start)

# list
start = time.time()

for i in range(100000000):
    lst.pop()

end = time.time()
print("list pop:", end - start)