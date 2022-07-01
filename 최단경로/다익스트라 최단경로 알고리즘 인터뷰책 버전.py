# (참고) 리트 코드 743번 문제. ( 책 기준 40번 )
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








------------------------------------------------------------
# 내 풀이 
import heapq

def networkDelayTime(times, n: int, k: int) -> int:
    INF = int(1e9)
    distance = [INF] * (n+1)
    
    distance[k] = 0
    q = []
    heapq.heappush(q,(0,k))
    

    while q: 
        # 가장 짧은 거리 노드 꺼내기
        dist, now = heapq.heappop(q)
        #현재 노드가 이미 처리된 적 있으면 무시 ( 최단 경로가 더 작은게 이미 있다면 )
        if distance[now] < dist:
            continue
        # 현재 노드와 연결된 다른 노드 확인
        for i in times:
            if i[0] != now :
                continue
            cost = dist + i[2]
            #현재 노드를 거쳐서, 다른 노드로 이동하는 거리가 더 짧은 경우
            if cost < distance[i[1]]:
                distance[i[1]] = cost
                heapq.heappush(q, (cost, i[1]))
                
    
    distance[0] = -1
    if INF in distance :
        return -1
    else:
        return max(distance)
    
print(networkDelayTime([[2,1,1],[2,3,1],[3,4,1]],4,2))
