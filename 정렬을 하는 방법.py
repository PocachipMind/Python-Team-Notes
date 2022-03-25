n = int(input())
students = []

# 학생 정보 받기
for _ in range(n):
    #students.append(input().split())
    name, k, e, m = input().split()
    students.append((name,k,e,m))

# Junkyu 50 60 100 와같이 n의 갯수만큼 이름, 국어, 영어, 수학 순으로 들어온다.

'''
[정렬 기준]
1) 두 번째 원소를 기준으로 내림차순 정렬
2) 두 번째 원소가 같은 경우, 세 번째 원소를 기준으로 오름차순 정렬
3) 세 번째 원소가 같은 경우, 네 번째 원소를 기준으로 내림차순 정렬
4) 네 번째 원소가 같은 경우, 첫 번째 원소를 기준으로 오름차순 정렬
'''


students.sort(key=lambda x: (-int(x[1]), int(x[2]), -int(x[3]), x[0]))

for student in students:
    print(student[0])
