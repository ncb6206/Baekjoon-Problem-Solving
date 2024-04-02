import sys
input = sys.stdin.readline

n = int(input())
switch = list(map(int,input().split()))
students = int(input())

for _ in range(students):
    gender, num = map(int,input().split())
    
    if gender == 1:
        for a in range(len(switch)):
            if (a+1) % num == 0:
                if switch[a] == 0:
                    switch[a] = 1
                else:
                    switch[a] = 0
                    
    else:
        i = 0
        while num - 1 + i < len(switch) and 0 <= num - 1 - i:
            if num - 1 + i == num - 1 - i:
                if switch[num - 1] == 0:
                    switch[num - 1] = 1
                else:
                    switch[num - 1] = 0
                      
            elif switch[num - 1 + i] == switch[num - 1 - i]:
                if switch[num - 1 + i] == 0:
                    switch[num - 1 + i] = 1
                else:
                    switch[num - 1 + i] = 0
                    
                if switch[num - 1 - i] == 0:
                    switch[num - 1 - i] = 1
                else:
                    switch[num - 1 - i] = 0
            else:
                break                   
            i += 1


for i in range(0,len(switch),20):
    for j in range(i,min(i+20,len(switch))):
        print(switch[j], end=" ")
    print()