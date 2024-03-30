import sys
from collections import defaultdict
input = sys.stdin.readline

N, M = map(int,input().split())
answer = defaultdict(int)
answers = []

for i in range(N+M):
    word = input().rstrip()
    if answer[word]:
        answers.append(word)
    answer[word] += 1

print(len(answers))
print('\n'.join(sorted(answers)))