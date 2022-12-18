T = int(input())

for _ in range(T):
    R,S = map(str,input().split())
    array = list(S)
    for i in array:
        for _ in range(int(R)):
            print(i,end="")
    print("")
