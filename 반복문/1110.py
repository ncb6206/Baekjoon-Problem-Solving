# 풀었긴 했지만 알고리즘이 보기 힘듬
N = input()
count = 0
T=N

while True:
    if(int(T)<10):
        hap = str(int(T))
        T = int(str(int(T)) + hap)
        count += 1

    else:
        T = str(T)
        hap = str(int(T[0])+int(T[1]))

        if(int(hap)<10):
            T = int(T[1] + hap[0])
        else:
            T = int(T[1]+hap[1])

        count += 1

    if(N==str(T)):
        print(count)
        break

# 정석 정답
'''
n=int(input())
num = n
cnt = 0

while True:
    a = num // 10
    b = num % 10
    c = (a+b)%10
    num = (b*10)+c
    cnt += 1
    if(num == n):
        break
        
print(cnt)
'''