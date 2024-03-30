import sys
input = sys.stdin.readline

N = int(input())
M = int(input())
S = input()

pattern = 0
count = 0

for i in range(M):
    pattern = 0
    if S[i:i+3] == 'IOI':
        pattern += 1
        j = i+3
        while j <= M:
            if pattern == N:
                count += 1
                break
            if S[j:j+2] != 'OI':
                break
            pattern += 1
            j += 2

print(count)