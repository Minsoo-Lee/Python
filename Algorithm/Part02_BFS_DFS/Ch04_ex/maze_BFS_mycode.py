# 동빈이는 N*M 크기의 직사각형 형태의 미로에 갇혔다.
# 초기 위치는 (1, 1)이며 미로의 출구는 (N, M)에 위치한다.
# 한 번에 한 칸만 이동할 수 있다.
# 괴물이 있는 부분은 0으로, 괴물이 없는 부분은 1로 표시되어 있다.
# 미로를 탈출하기 위해 움직여야 하는 최소 칸의 개수를 구하라
# 칸을 셀 때는 시작 칸과 마지막 칸을 모두 포함해서 계산한다.

# 또 실패

from collections import deque

def bfs(y, x):
    dir = ((0, 1), (-1, 0), (0, -1), (1, 0))
    queue = deque()
    queue.append((y, x))
    count = 2
    while queue:
        v = queue.popleft()
        for i in dir:
            dx = x + i[1]
            dy = y + i[0]
            if graph[dx][dy] == 1:
                graph[dx][dy] = count
                count += 1
            
    
n, m = map(int, input().split())
graph = []
for i in range(m):
    graph.append(list(map(int, input().split())))

