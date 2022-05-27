# 리트코드 41문제.
# k+1 해서 k가 일정 수치보다 높을시 안할수도있지만, 간결성을 위해 1씩 빼는걸로 바뀜

import heapq
import collections

def findCheapestPrice(n: int, flights, src: int, dst: int, k: int) -> int:
    graph = collections.defaultdict(list)
    # 그래프 인접 리스트 구성
    for u, v, w in flights:
        graph[u].append((v,w))
        
    # 큐 변수 : [(가격, 정점, 남은 가능 경유지 수)]
    Q = [(0, src, k)]
    
    # 우선순위 큐 최솟값기준으로 도착점까지 최소 비용 판별
    while Q:
        price, node, k = heapq.heappop(Q)
        if node == dst:
            return price
        if k >= 0:
            for v, w in graph[node]:
                alt = price + w
                heapq.heappush(Q,(alt, v, k-1))
    return -1
    
print(findCheapestPrice(4,[[0,1,100],[1,2,100],[2,0,100],[1,3,600],[2,3,200]],0,3,1))
