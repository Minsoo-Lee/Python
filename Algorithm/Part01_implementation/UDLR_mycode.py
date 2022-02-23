# 여행가 A는 N X N 크기의 정사각형 위에 서 있다.
# 가장 왼쪽 위 좌표는 (1, 1)이며, 가장 오른쪽 아래 좌표는 (N, N)에 해당한다.
# 여행가 A는 상하좌우 방향으로 이동할 수 있으며, 한 칸 이동이 가능하다. 

n = map(int, input().split())
move = list(input().split())
pos = [1, 1]

for dir in move:
    x = 0
    y = 0
    if dir == "R":
        x += 1
    elif dir == "L":
        x -= 1
    elif dir == "U":
        y -= 1
    elif dir == "D":
        y += 1
    if pos[1] + x < 1 or pos[1] + x > 5:
        continue
    elif pos[0] + y < 1 or pos[0] + y > 5:
        continue
    else:
        pos[1] += x
        pos[0] += y
    print(pos[0], pos[1])
print(pos[0], pos[1])