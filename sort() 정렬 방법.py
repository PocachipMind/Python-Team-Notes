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

    

    # 내림차순은 음수 붙이기!  순서대로 튜플로 쓰기!
    
    
   


...
...

# 또다른 예시
'''
[정렬 기준]
1) 로그의 가장 앞 부분은 식별자다.
2) 문자로 구성된 로그가 숫자 로그보다 앞에 온다.
3) 식별자는 순서에 영향을 끼치지 않지만, 문자가 동일할 경우 식별자 순으로 한다.
4) 숫자 로그는 입력 순서대로 한다.
'''

# 입력 - logs = ["dig1 8 1 5 1", "let1 art can", "dig2 3 6", "let2 own kit dig", "let3 art zero"]
# 출력 - [ "let1 art can", "let3 art zero", "let2 own kit dig", "dig1 8 1 5 1" , "dig2 3 6"]

def reorderLogFiles(logs : List[str]) -> List[str]:
    letters, digits = [], []
    for log in logs:
        if log.split()[1].isdigit():
            digits.append(log)
        else:
            letters.append(log)
    
    # 2개의 키를 람다 표현식으로 정렬
    letters.sort(key=lambda x: (x.split()[1:], x.split()[0]))
    return letters + digits


                
