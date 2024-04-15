# if not student[i]를 사용하는 과정에서 defaultdict가 자동으로 student딕셔너리에 존재하지 않는 값을
# 추가해줘서 list(student)에 i값이 들어가는 경우가 발생하여 list(student)에서 맨 뒤에 있는 요소를 빼는 형식으로 구현

import sys
from collections import defaultdict
input = sys.stdin.readline

N = int(input())                                    # 사진틀의 개수 입력받기
chucheon = int(input())                             # 추천 횟수 입력받기
student = defaultdict(int)                          # 학생 별 추천 횟수를 저장할 딕셔너리
recommend = list(map(int,input().split()))          # 추천받은 학생 번호 입력받기

# 추천받은 학생에 대해
for i in recommend:
    # 사진틀에 여유가 있다면 해당 학생의 추천 횟수를 1 증가시킴
    if len(student) < N:    
        student[i] += 1
        
    # 사진틀이 꽉 찼을 경우
    else:
        # 해당 학생의 사진이 사진틀에 없다면
        if not student[i]:
            listStudent = list(student)[:-1]    # 사진틀에 있는 학생들을 리스트로 저장하되, 마지막 학생은 제외
            temp = listStudent[0]               # 가장 오래된 학생의 번호를 임시로 저장
            # 사진틀에 있는 학생들을 탐색 
            for j in listStudent:
                # 추천 횟수가 더 적은 학생을 찾으면 해당 학생의 번호로 임시 저장
                if student[j] < student[temp]:          
                    temp = j            
            student.pop(temp)                   # 가장 추천 횟수가 적고 가장 오래된 학생의 사진을 제거            
            student[i] += 1                     # 새로운 학생의 추천 횟수를 1 증가시킴
        # 해당 학생의 사진이 사진틀에 이미 있다면 해당 학생의 추천 횟수를 1 증가시킴
        else:
            student[i] += 1

 # 사진틀에 있는 학생들의 번호를 오름차순으로 출력
print(*sorted(list(student)))