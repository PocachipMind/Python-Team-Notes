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

#union 연산 각각 수행
for i in range(e):
    a, b = map(int,input().split())
    union_parent(parent,a,b)

