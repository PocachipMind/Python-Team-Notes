# 2차원 리스트 90도 회전
def rotate_a_matrix_by_90_degree(a):
    row_length = len(a)  # 행길이 계산
    column_length = len(a[0]) # 열 길이 계산

    res = [[0] * row_length for _ in range(column_length)] # 결과 리스트
    for r in range(row_length):
        for c in range(column_length):
            res[c][row_length - 1 - r] = a[r][c]

    return res
  
  # 이 코드는 나동빈님의 "이것이 취업을 위한 코딩 테스트이다." 책과
  # "https://github.com/ndb796/Python-Competitive-Programming-Team-Notes/blob/master/Miscellaneous/rotate_a_matrix_by_90_degree.py" 를 참고하여 작성되었습니다.
