import sys
input = sys.stdin.readline

N,M = map(int,input().split())

chess = [list(input().rstrip()) for _ in range(N)]
minArray = []

for a in range(N-7):
    for b in range(M-7):
        countB = 0
        countW = 0
        for i in range(a,a+8):
            for j in range(b,b+8):
                if (i+j) % 2 == 0:
                    if chess[i][j] != "B":
                        countB += 1
                    if chess[i][j] != "W":
                        countW += 1
                else:
                    if chess[i][j] != "W":
                        countB += 1
                    if chess[i][j] != "B":
                        countW += 1
        minArray.append(min(countB,countW))
        
print(min(minArray))