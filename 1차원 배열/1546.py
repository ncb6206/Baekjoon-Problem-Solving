N = int(input())
array = list(map(int,input().split()))
hap = 0

for i in array:
    hap += i/max(array)*100

print(hap/N)


