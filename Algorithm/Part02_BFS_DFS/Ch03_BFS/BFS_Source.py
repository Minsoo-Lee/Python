from collections import deque
# BFS 메서드 정의
def bfs(graph, start, visited):
    # 큐 구현을 위해 deque 라이브러리 사용
    queue = deque([start])
    # 현재 노드를 방문 처리
    visited[start] = True
    # 큐가 빌 때까지 반복
    while queue:
        # 큐에서 하나의 원소를 뽑아 출력하기
        v = queue.popleft()
        print(v, end = ' ')
        # 아직 방문하지 않은 인접한 원소들을 큐에 삽입
        for i in graph[v]:
            if not visited[i]:
                queue.append(i)
                visited[i] = True

# 각 노드가 연결된 정보를 표현(2차원 리스트)
graph = [
    [],
    [2, 3, 8],
    [1, 7],
    [1, 4, 5],
    [3, 5],
    [3, 4],
    [7],
    [2, 6, 8],
    [1, 7]
]

# 각 노드가 방문된 정보를 표현
visited = [False] * 9

bfs(graph, 1, visited)
# visited = [F T F F F F F F F]     queue = [1]             v = NULL       
# visited = [F T T T F F F F T]     queue = [2, 3, 8]       v = 1
# visited = [F T T T F F F T T]     queue = [3, 8, 7]       v = 2
# visited = [F T T T T T F T T]     queue = [8, 7, 4, 5]    v = 3
# visited = [F T T T T T F T T]     queue = [7, 4, 5]       v = 8
# visited = [F T T T T T T T T]     queue = [4, 5, 6]       v = 7
# visited = [F T T T T T T T T]     queue = [5, 6]          v = 4
# visited = [F T T T T T T T T]     queue = [6]             v = 5
# visited = [F T T T T T T T T]     queue = []              v = 6