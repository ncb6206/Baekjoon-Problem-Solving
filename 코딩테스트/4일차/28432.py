import sys
input = sys.stdin.readline

N = int(input())
answer = []
index = 0
first,last = "",""

for i in range(N):
    word = input().rstrip()
    if word == "?":
        index = i
    answer.append(word)

first = answer[index-1][-1]

if index != N-1:
    last = answer[index+1][0]

M = int(input())

for _ in range(M):
    word = input().rstrip()
    if first == word[0] and last == word[-1]:
        if not word in answer:
            print(word)