import sys
input = sys.stdin.readline

N = int(input())
M = int(input())
S = input()

pattern = 0
count = 0
i = 0

while i <= M:
    if S[i:i+3] == 'IOI':
        pattern += 1
        i += 2
        if pattern == N:
            count += 1
            pattern -= 1    
    else:
        i += 1
        pattern = 0        

print(count)