# 내가 짠 코드는 아님

import sys
input = sys.stdin.readline

N,M,R = map(int,input().split())

nemo = [list(input().split()) for _ in range(N)]

for _ in range(R):
    for i in range(min(N,M)//2):
        x,y = i,i
        value = nemo[x][y]
        
        for j in range(i+1,N-i):
            x = j
            temp = nemo[x][y]
            nemo[x][y] = value
            value = temp
        
        for j in range(i+1, M-i):
            y = j
            temp = nemo[x][y]
            nemo[x][y] = value
            value = temp
            
        for j in range(i+1, N-i):
            x = N - j - 1
            temp = nemo[x][y]
            nemo[x][y] = value
            value = temp
        
        for j in range(i+1,M-i):
            y = N - j - 1
            temp = nemo[x][y]
            nemo[x][y] = value
            value = temp
            
for i in nemo:
    print(*i)          