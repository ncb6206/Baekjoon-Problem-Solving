# 직접 푼 알고리즘
T = int(input())

for _ in range(T):
    R,S = map(str,input().split())
    array = list(S)
    for i in array:
        for _ in range(int(R)):
            print(i,end="")
    print("")

# 인터넷에서 찾은 정답 알고리즘
'''
T = int(input())

for i in range(T):
    num, s = input().split()
    text = ''
    for i in s:
        text += int(num) * i
    print(text)
'''