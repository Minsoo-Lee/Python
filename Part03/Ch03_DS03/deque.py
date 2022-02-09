# deque : stack + queue
from collections import deque
deque_list = deque()
print(deque_list)
for i in range(5):
    deque_list.append(i)
print(deque_list)

# pop(0) X
print(deque_list.pop())
print(deque_list.pop())
print(deque_list.pop())
print(deque_list)

# appendleft()
deque_list.clear()
for i in range(5):
    deque_list.appendleft(i)
print(deque_list)

# rotate()
deque_list.rotate(1)
print(deque_list)
deque_list.rotate(-1)
print(deque_list)

# reversed()
print(deque(reversed(deque_list)))

# extend() / extendleft()
deque_list.extend([5, 6, 7])
print(deque_list)
deque_list.extendleft([7, 6, 5])
print(deque_list)

# deque()
base = ["a", "b", "c", "d", "e"]
deque_list = deque(base, maxlen=3)
print(deque_list)
print(deque_list.popleft())
print(deque_list)