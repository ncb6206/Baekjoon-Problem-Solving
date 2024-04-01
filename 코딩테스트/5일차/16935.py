# 내가 짠 코드는 아닌데 진짜 잘 짠 코드여서 기록

import sys
input = sys.stdin.readline

N,M,R = map(int,input().split())

nemo = [list(input().split()) for _ in range(N)]
cache = nemo
wayList = list(map(int,input().split()))

for way in wayList:
    x = len(cache[0])
    y = len(cache)
    temp = []
    
    if way == 1:
        for i in range(y):
            temp1 = []
            for j in range(x):
                temp1.append(cache[y-1-i][j])
            temp.append(temp1)
    elif way == 2:
        for i in range(y):
            temp1 = []
            for j in range(x):
                temp1.append(cache[i][x-1-j])
            temp.append(temp1)                
    elif way == 3:
        for i in range(x):
            temp1 = []
            for j in range(y):
                temp1.append(cache[y-1-j][i])
            temp.append(temp1)
    elif way == 4:
        for i in range(x):
            temp1 = []
            for j in range(y):
                temp1.append(cache[j][x-1-i])
            temp.append(temp1)
    elif way == 5:
        temp1, temp2, temp3, temp4 = [], [], [], []
        for i in range(y):
            if y//2 > i:
                temp1.append(cache[i][:x//2])
                temp2.append(cache[i][x//2:])
            else:
                temp4.append(cache[i][:x//2])
                temp3.append(cache[i][x//2:])
                
        for j in range(len(temp1)):
            temp.append(temp4[j]+temp1[j])
        for j in range(len(temp1)):
            temp.append(temp3[j]+temp2[j])
    elif way == 6:
        temp1, temp2, temp3, temp4 = [], [], [], []
        for i in range(y):
            if y//2 > i:
                temp1.append(cache[i][:x//2])
                temp2.append(cache[i][x//2:])
            else:
                temp4.append(cache[i][:x//2])
                temp3.append(cache[i][x//2:])
                
        for j in range(len(temp2)):
            temp.append(temp2[j]+temp3[j])
        for j in range(len(temp1)):
            temp.append(temp1[j]+temp4[j])
    
    cache = temp

for list in cache:
    print(*list)
