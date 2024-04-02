import sys
from itertools import combinations
input = sys.stdin.readline

n,m = map(int,input().split())
Map = [list(map(int,input().split())) for _ in range(n)]
chicken = []
house = []
answer = int(1e9)

for i in range(n):
    for j in range(n):
        if Map[i][j] == 1:
            house.append((i+1,j+1))           
        elif Map[i][j] == 2:
            chicken.append((i+1,j+1))

chickenComb = list(combinations(chicken,m))
         
for comb in chickenComb:
    temp = [1e9] * len(house)
    for dak in comb:              
        for i in range(len(house)):     
            # 이를 이용해서 해당 순열의 경우중 가장 작은 값을 찾을 수 있음(이 줄이 이 문제 핵심)
            temp[i] = min(temp[i],(abs(dak[1]-house[i][1]) + abs(dak[0]-house[i][0])))
        
        answer = min(answer,sum(temp))
        
print(answer)        