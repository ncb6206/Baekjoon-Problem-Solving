N = int(input())
hansu = 0

if(N<100):
    hansu += N
else:
    hansu+=99

    for i in range(100,N+1):
        array = list(str(i))
        if(int(array[0])-int(array[1])==int(array[1])-int(array[2])):
            hansu += 1

print(hansu)