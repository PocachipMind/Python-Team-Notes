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




---------------------------------------------------------------------------------------------------------------------------------------
# 거리 2 이하인곳 찾는 그거인데, 약간 이런식으로 구현하는거 익혀둬야함.
from collections import deque

#    북  동  남 서 
dx = [-1, 0, 1, 0]
dy = [ 0, 1, 0,-1]

def bfs(place,i,j):
    q = deque()
    visited = []
    q.append((i,j,0))
    visited.append((i,j))
    
    while q:
        x,y,cost = q.popleft()
        
        if place[x][y] == "X":
            continue
        if cost >= 3:
            continue
        if place[x][y] == "P" and cost != 0:
            return False
        
        for nxt in range(4):
            nx = x + dx[nxt]
            ny = y + dy[nxt]
            if nx <0 or ny <0 or nx >= 5 or ny >=5:
                continue
            if not (nx,ny) in visited:
                q.append((nx,ny,cost+1))
                visited.append((nx,ny))
                
    return True
