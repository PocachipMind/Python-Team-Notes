# 너비 우선 탐색(BFS)를 통해 최단거리를 파악합니다
# 카카오 2020 기출문제 정답 코드 일부 발췌

import collections
def solution():
     
    q = collections.deque()

    visited = []
    pos = {(1,1),(1,2)} # 시작 위치 설정
    q.append((pos,0)) # 큐에 삽입한 뒤에
    visited.append(pos) # 방문 처리

    # 큐가 빌 때까지 반복
    while q:
        pos, cost = q.popleft()
        # ( n, n ) 위치에 로봇이 도달했다면, 최단 거리이므로 반환
        if (n, n) in pos:
            return cost
        # 현재 위치에서 이동할 수 있는 위치 확인
        for next_pos in get_next_pos(pos, new_board):
            # 아직 방문하지 않은 위치라면 큐에 삽입하고 방문 처리
            if next_pos not in visited:
                q.append((next_pos, cost +1))
                visited.append(next_pos)
    
    return 0

