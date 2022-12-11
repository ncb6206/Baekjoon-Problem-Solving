# 답 안보고 풀은 알고리즘
N = int(input())

for _ in range(N):
    score = 0
    stack = 0
    quiz = input()

    for i in range(len(quiz)):
        if(quiz[i]=="O"):
            score += (1+stack)
            stack += 1
        else:
            stack = 0

    print(score)

# 답 참고한 알고리즘
'''
N = int(input())

for _ in range(N):
    quiz = list(input())
    score = 0
    stack = 0

    for i in quiz:
        if(i=="O"):
            score += (1+stack)
            stack += 1
        else:
            stack = 0

    print(score)
'''