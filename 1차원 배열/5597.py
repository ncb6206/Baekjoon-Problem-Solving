array = list()

for _ in range(28):
    array.append(int(input()))

for i in range(1,31):
    if(array.count(i)==0):
        print(i)