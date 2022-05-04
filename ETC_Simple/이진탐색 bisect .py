...
bisect.bisect_left(정렬된리스트,값)     
bisect.bisect_right(정렬된리스트,값)   

정렬된 순서를 유지하면서 리스트에 데이터를 삽입할 가장 (왼쪽/오른쪽) 인덱스를 찾는 메서드


만약 4라면
1  2  4  4  8 
     ↑     ↑
    (2)   (4)
...



from bisect import bisect_left, bisect_right

# 값이 [left_value, right_value]인 데이터의 개수를 반환하는 함수
def count_by_range(a, left_value, right_value):
    right_index = bisect_right(a, right_value)
    left_index = bisect_left(a, left_value)
    return right_index - left_index
 
# 리스트 선언
a = [ 1, 2, 3, 3, 3, 3, 4, 4, 8, 9]

#값이 4인 데이터 개수 출력
print(count_by_range(a,4,4))
# 2


#값이 [-1, 3] 범위에 있는 데이터 개수 출력
print(count_by_range(a,-1,3))
# 6
