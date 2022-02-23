# 체스에서 현재 위치가 주어졌을 때, 나이트가 이동할 수 있는 경우의 수를 구하시오
# 현재 위치는 a1 / h5와 같이 알파벳+숫자로 주어진다.

str = input()
x, y = (ord(str[0]) - ord('a')), (ord(str[1]) - ord('1'))

one = [1, -1]
two = [2, -2]
count = 0

for dx in one:
    for dy in two:
        if dx + x >= 0 and dx + x <= 7 and dy + y >= 0 and dy + y <= 7:
            count += 1
        if dy + x >= 0 and dy + x <= 7 and dx + y >= 0 and dx + y <= 7:
            count += 1
            
print(count)