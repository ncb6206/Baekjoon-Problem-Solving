import sys

N = int(sys.stdin.readline())
grades = list(map(int,sys.stdin.readline().split()))
newGrade = list()

for i in grades:
    newGrade.append(i/max(grades)*100)

print(round(sum(newGrade)/N,6))