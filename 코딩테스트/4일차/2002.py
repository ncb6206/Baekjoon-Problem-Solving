import sys
from collections import defaultdict
input = sys.stdin.readline

N = int(input())
inCar = defaultdict(int)
outCar = []
count = 0

for i in range(N):
    car = input().rstrip()
    inCar[car] = i

for i in range(N):
    car = input().rstrip()
    outCar.append(car)

for i in range(N-1):
    now_out = inCar[outCar[i]]
    for j in range(i+1,N):
        next_out = inCar[outCar[j]]
        if next_out < now_out:
            count += 1
            break

print(count)