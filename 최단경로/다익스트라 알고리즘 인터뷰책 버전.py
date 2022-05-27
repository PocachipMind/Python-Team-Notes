# (참고) 리트 코드 40번 문제.
# 특정 노드에서 출발하여 다른 노드로가는 최단경로 구하기

import heapq
import collections

def networkDelayTime(times, n: int, k: int) -> int:
    graph = collections.defaultdict(list)
    # 그래프 인접 리스트 구성
    
    for u, v, w in times:
        graph[u].append((v,w))
    
    # 큐변수 : [(소요시간, 정점)]
    q = [(0,k)]
    dist = collections.defaultdict(int)
    
    # 우선순위 큐 최솟값 기준으로 정점까지 최단 경로 삽입
    while q:
        time, node = heapq.heappop(q)
        if node not in dist:
            dist[node] = time
            for v, w in graph[node]:
                alt = time + w
                heapq.heappush(q,(alt,v))
                
    if len(dist) == n :
        return max(dist.values())
    return -1
    
print(networkDelayTime([[2,1,1],[2,3,1],[3,4,1]],4,2))
