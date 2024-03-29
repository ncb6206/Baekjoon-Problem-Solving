import sys
from itertools import combinations
input = sys.stdin.readline

N,M = map(int,input().split())
array = list()
answer = []
answers = []

# for i in range(N):
#     array.append(i+1)
#
# for j in combinations(array,M):
#     print(*j)

def back_tracking(index,n,m,start):
    if index == m:
        answers.append(' '.join(map(str,answer)))
        return
    for i in range(start,n):
        answer.append(i+1)
        back_tracking(index+1,n,m,i+1)
        answer.pop()

back_tracking(0,N,M,0)

print('\n'.join(answers))