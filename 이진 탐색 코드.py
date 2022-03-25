

#  재귀함수 이진탐색
def binary_search_recursion(array, target, start, end):
    if start > end:
        return None
    mid = (start + end) //2
    # 찾은경우 중간 인덱스 반환
    if array[mid] == target:
        return mid
    #중간점 보다 찾으려는게 값이 작음 > 왼쪽
    elif array[mid] > target:
        return binary_search_recursion(array, target, start, mid-1)
    #중간점 보다 찾으려는게 큼 > 오른쪽
    elif array[mid] < target:
        return binary_search_recursion(array, target, mid+1, end)
    
    



# 반복문으로 작성된 이진 탐색
def binary_search_iteration(array, target, start, end):
    while start <= end:
        mid = (start + end) // 2
        #찾았다!
        if array[mid] == target:
            return mid
        #중간보다 찾으려는게 작으면 왼쪽
        elif array[mid] > target:
            end = mid - 1
        #중간보다 찾으려는게 크면 오른쪽
        else :
            start = mid + 1
    #결국 못찾음.
    return None
