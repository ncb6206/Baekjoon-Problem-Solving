import sys
from itertools import permutations
input = sys.stdin.readline
answers = []

name = list(input().rstrip())
answer = list(set(permutations(name,len(name))))

for i in answer:
    if ''.join(i) == ''.join(i)[::-1]:
        answers.append(''.join(i))

if answers:
    print(sorted(answers)[0])
else:
    print("I'm Sorry Hansoo")
