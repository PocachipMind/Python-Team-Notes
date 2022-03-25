# 특정 원소가 속한 집합 찾기
def find_parent(parent,x):
    #루트 노드가 아니면 루트노드 찾기
    if parent[x] != x:
        parent[x] = find_parent(parent, parent[x])
    return parent[x]

#두 원소가 속한 집합 합치기
def union_parent(parent, a, b):
    a = find_parent(parent,a)
    b = find_parent(parent,b)
    if a < b:
        parent[b] = a
    else :
        parent[a] = b
        

v , e = 노드개수, 간선(union 연산)
parent = [0] * (v + 1) # 부모테이블 초기화

#부모테이블 자기자신을 부모로 초기화
for i in range(1, v+1):
    parent[i] = i
    


########################################



# 모든 간선을 담을 리스트와 최종 비용담을 변수
edges = []
result = 0

for _ in range(e):
    a, b, cost = map(int, input().split())
    #비용순으로 정렬하기 위해서 튜플의 첫 원소가 비용
    edges.append((cost,a,b))
    
# 간선 비용순 정렬
edges.sort()

# 간선 하나씩 확인하며
for edge in edges:
    cost , a, b = edge
    # 사이클이 발생하지 않는 경우에만 집합에 포함
    if find_parent(parent,a) != find_parent(parent,b):
        union_parent(parent, a, b)
        result += cost
        
print(result)
