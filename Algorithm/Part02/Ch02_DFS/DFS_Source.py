# DFS 메서드 정의
def dfs(graph, v, visited):
    # 현재 노드를 방문 처리
    visited[v] = True
    print(v, end = ' ')
    # 현재 노드와 연결된 다른 노드를 재귀적으로 방문
    for i in graph[v]:
        if not visited[i]:
            dfs(graph, i, visited)
            
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

dfs(graph, 1, visited)
# visited = [F T F F F F F F F]
# visited = [F T T F F F F F F]
# visited = [F T T F F F F T F]
# visited = [F T T F F F T T F]
# visited = [F T T F F F T T T]
# visited = [F T T T F F T T T]
# visited = [F T T T T F T T T]
# visited = [F T T T T T T T T]
# 1 2 7 6 8 3 4 5