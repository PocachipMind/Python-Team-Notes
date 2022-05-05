# 특정 노드에서 출발하여 다른 노드로가는 최단경로 구하기

import heapq
import sys
inpuit = sys.stdin.readline
INF = int(1e9)

n , m = 노드개수, 간선수

start = 시작노드

graph = [[] for _ in range(n+1)]

distance = [INF] * n+1

# 간선 정보 입력 받기
for _ in range(m):
    a, b, c = map(int, input().split())
    # a에서 b로 가는비용이 c임
    graph[a].append((b,c))
    

def dijkstra(start):
    q = []
    # 시작 노드로 가기위한 경로는 0으로 큐 삽입
    heapq.heappush(q,(0,start))
    distance[start] = 0
    
    #q가 비어있지 않다면
    while q: 
        # 가장 짧은 거리 노드 꺼내기
        dist, now = heapq.heappop(q)
        #현재 노드가 이미 처리된 적 있으면 무시 ( 최단 경로가 더 작은게 이미 있다면 )
        if distance[now] < dist:
            continue
        # 현재 노드와 연결된 다른 노드 확인
        for i in graph[now]:
            cost = dist + i[1]
            #현재 노드를 거쳐서, 다른 노드로 이동하는 거리가 더 짧은 경우
            if cost < distance[i[0]]:
                distance[i[0]] = cost
                heapq.heappush(q, (cost, i[0]))
