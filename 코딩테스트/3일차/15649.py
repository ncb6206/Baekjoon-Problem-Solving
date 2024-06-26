import sys
from itertools import permutations
input = sys.stdin.readline

N, M = map(int,input().split())
visited = [False] * N
answers = []
answer = []
# for i in range(N):
#     array.append(i+1)
#
# for dap in permutations(array,M):
#     print(*dap)

def back_tracking(index,n,m):
    if index == m:
        answers.append(' '.join(map(str,answer)))
        return
    for i in range(n):
        if not visited[i]:
            visited[i] = True
            answer.append(i+1)
            back_tracking(index+1,n,m)
            visited[i] = False
            answer.pop()

back_tracking(0,N,M)

print('\n'.join(answers))