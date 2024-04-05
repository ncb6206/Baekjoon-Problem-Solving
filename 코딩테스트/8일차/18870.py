import sys
input = sys.stdin.readline

n = int(input())
x = list(enumerate(map(int,input().split())))
x.sort(key = lambda x: x[1])

result = [0] * n
count = 0

for i in range(1,len(x)):
    if x[i][1] != x[i-1][1]:
        count += 1
        result[x[i][0]] = count
    else:
        result[x[i][0]] = count

print(*result)