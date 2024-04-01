import sys
input = sys.stdin.readline

N = int(input())

room = [list(input().rstrip()) for _ in range(N)]

garoCount = 0
seroCount = 0
garo = 0
sero = 0

for i in range(N):
    garoCount = 0
    seroCount = 0
    for j in range(N):
        if room[i][j] == '.':
            garoCount += 1
            if j == N-1 and garoCount >= 2:
                garo += 1
        else:
            if garoCount >= 2:
                garo += 1
            garoCount = 0
                
        if room[j][i] == '.':
            seroCount += 1
            if j == N-1 and seroCount >= 2:
                sero += 1
        else:
            if seroCount >= 2:
                sero += 1
            seroCount = 0

print(f"{garo} {sero}")