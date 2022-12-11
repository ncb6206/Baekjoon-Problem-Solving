array = list()
count = 0

for _ in range(10):
    array.append(int(input())%42)

for i in range(42):
    if(array.count(i)!=0):
        count += 1

print(count)