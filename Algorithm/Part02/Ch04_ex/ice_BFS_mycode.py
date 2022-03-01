# N*M 크기의 얼음 틀이 있습니다.
# 구멍이 뚫려 있는 부분은 0, 칸막이가 존재하는 부분은 1
# 구멍이 뚫려 있는 부분끼리 상, 하, 좌, 우로 붙어 있는 경우 서로 연결되어 있는 것으로 간주
# 얼음 틀의 모양이 주어졌을 때 생성되는 총 아이스크림의 개수를 구하는 프로그램을 작성하시오

# 시간초과 실패
# 이건 BFS가 아닌 DFS로 푸는 게 맞는 거 같다

# BFS
from collections import deque

def check_point(x, y):
    if x >= 0 and y >= 0 and x < m and y < n:
        return True
    return False

def bfs(x, y, visited):
    d = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    queue = deque()
    if (visited[y][x] == 1):
        return False
    visited[y][x] = 1
    queue.append((y, x))
    while queue:
        print(queue)
        v = queue.popleft()
        for i in d:
            dx = x + i[1]
            dy = y + i[0]
            check = False
            if check_point(dx, dy) == True:
                if visited[dy][dx] == 0:
                    check = True
        if check == False:
                y += 1
                x = 0
                if check_point(x, y) and visited[y][x] == 1:
                    return True
        for i in d:
            dx = x + i[1]
            dy = y + i[0]
            if check_point(dx, dy) == True:
                if graph[dy][dx] == 0:
                    x, y= dx, dy
                    queue.append((y, x))
                    visited[y][x] = 1
    print()
    return True

graph = [
    [0, 0, 1, 1, 0],
    [0, 0, 0, 1, 1],
    [1, 1, 1, 1, 1],
    [0, 0, 0, 0, 0],
]

visited = [
    [0, 0, 1, 1, 0],
    [0, 0, 0, 1, 1],
    [1, 1, 1, 1, 1],
    [0, 0, 0, 0, 0],
]

n, m = 4, 5
result = 0
for i in range(m):
    for j in range(n):
        if bfs(i, j, visited) == True:
          result += 1  
print(result)
