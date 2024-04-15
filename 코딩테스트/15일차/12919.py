import sys
input = sys.stdin.readline

S = list(input().rstrip())
T = list(input().rstrip())
needA = T.count('A')
needB = T.count('B')
countA = S.count('A')
countB = S.count('B')
can = 0

def bfs(word):
    global countA,countB,can,needA,needB
    if countA < needA:
        word.append('A')
        countA += 1
        bfs(word)
        countA -= 1
    if countB < needB:
        word.append('B')
        countB += 1
        word.reverse()
        bfs(word)
        countB -= 1
    if len(word) == len(T):
        isTrue = True
        for i in range(len(word)):
            if word[i] != T[i]:
                isTrue = False
                break
        if isTrue:
            can = 1

bfs(S)        
print(can)