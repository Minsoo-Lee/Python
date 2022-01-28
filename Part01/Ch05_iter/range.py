#1. range(x)
sum = 0
for x in range(10):
    sum += x
print(sum)

#2. range(start, stop) : include start, exclude stop
sum = 0
for x in range(0, 10):
    sum += x
print(sum)

#3. range(start, stop, step) : include start, exclude stop, skip step
sum = 0
for x in range(0, 10, 3):
    sum += x
print(sum)

#4. 문자열 시퀀스
s = "Lee Min Soo"
for ch in s:
    print(ch, end = " ")