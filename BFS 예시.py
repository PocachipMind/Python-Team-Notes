from collections import deque

def bfs(graph, start, visited):
    # 큐 구현 위해 deque 라이브러리 사용
    queue = deque([start])
    # 현재 노드 방문 처리
    visited[start] = True
    # 큐가 빌 때까지 반복
    while queue:
        #큐에서 하나 원소 뽑아 출력
        v = queue.popleft()
        print(v, end=" ")
        #해당 원소와 연결된, 아직 방문하지 않은 원소들을 큐에 삽입
        for i in graph[v]:
            if not visited[i]:
                queue.append(i)
                visited[i] = True
                
                
                
                
                
n = 노드 수
m = 간선 수

graph = [[] for _ in range(n)]
          
for _ in range(m):
    a,b = map(int,input().split())
    graph[a].append(b)

visited = [False] * n



bfs(graph, 1, visited)
