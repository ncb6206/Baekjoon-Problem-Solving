import sys
input = sys.stdin.readline

N = int(input())
K = int(input())
sensor = list(map(int,input().split()))

if N <= K:
    print(0)
    exit(0)

sensor.sort()
diff = []

for i in range(1,N):
    diff.append(sensor[i]-sensor[i-1])
    
diff.sort()
result = diff[:(N-K)]

print(sum(result))