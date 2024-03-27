import sys

yoil = ["MON","TUE","WED","THU","FRI","SAT","SUN"]
day = [31,28,31,30,31,30,31,31,30,31,30,31]

x,y = map(int,sys.stdin.readline().split())

hap = 0

for i in range(x-1):
    hap = hap + day[i]

hap = hap + (y-1)

print(yoil[hap % 7])

