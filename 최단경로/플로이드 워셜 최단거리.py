INF = int(1e9)

n , m = 노드개수, 간선수


# 2차원 리스트(그래프 표현) 만들고 모든 값 무한으로
graph = [ [INF] * (n+1) for _ in range(n+1) ]

# 자기 자신으로 가는 비용 0
for i in range(n+1):
    graph[i][i] = 0
    
for _ in range(m):
    # a에서 b 가는 비용은 c임
    a, b, c = map(int,input().split())
    graph[a][b] = c
    

#플로이드 워셜 알고리즘
#k,a,b 잘맞
for k in range(1,n+1):
    for a in range(1, n+1):
        for b in range( 1, n+1):
            graph[a][b] = min(graph[a][b], graph[a][k] + graph[k][b])
