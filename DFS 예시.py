# 방문함과 동시에 visited 체크 할것
# dfs 메소드 정의
def dfs(graph, v, visited):
    # 현재 노드 방문 처리
    visited[v] = True
    print(v, end=" ")
    # 현재 노드와 연결된 다른 노드를 재귀적으로 방문
    for i in graph[v]:
        if not visited[i]:
            dfs(graph, i, visited)
            
           
          
          
          
n = 노드 수
m = 간선 수
graph = [[] for _ in range(n)]
          
for _ in range(m):
    a,b = map(int,input().split())
    graph[a].append(b)

visited = [False] * n
