# 정렬하는 거랑 정렬해놓으면 for문을 한번만 돌려도 답이 나온다는 게 포인트

import sys
input = sys.stdin.readline

N = int(input())
meeting = []

for _ in range(N):
    start,end = map(int,input().split())
    meeting.append([start,end])
    
meeting.sort(key=lambda x: (x[1],x[0]))

stack = []
stack.append([meeting[0][0],meeting[0][1]])

for i in range(1,N):
    start,end = meeting[i]
    if stack[-1][1] <= start:
        stack.append([start,end])

print(len(stack))