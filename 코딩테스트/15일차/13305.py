import sys
input = sys.stdin.readline

N = int(input())
road = list(map(int,input().split()))
oil = list(map(int,input().split()))
hap = 0
j = 0
temp = 0

for i in range(len(road)):
    if not hap:
        hap += (oil[j]*road[i])
    else:
        if oil[temp] > oil[j]:
            temp = j        
        hap += (oil[temp]*road[i])
    j += 1

print(hap)