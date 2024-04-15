import sys
from collections import defaultdict
input = sys.stdin.readline

N = int(input())
chucheon = int(input())
student = defaultdict(int)
recommend = list(map(int,input().split()))

for i in recommend:
    if len(student) < N:
        student[i] += 1
    else:
        if not student[i]:
            listStudent = list(student)[:-1]
            temp = listStudent[0]
            for j in listStudent:
                if student[j] < student[temp]:          
                    temp = j
            student.pop(temp)
            student[i] += 1       
        else:
            student[i] += 1

print(*sorted(list(student)))