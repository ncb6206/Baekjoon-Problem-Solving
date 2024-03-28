import sys

n = int(sys.stdin.readline())
people = {}
remain = list()

for _ in range(n):
    x1, x2 = map(str,sys.stdin.readline().split())
    people.update({x1:x2})

for name, inOut in people.items():
    if inOut == 'enter':
        remain.append(name)

for name in sorted(remain,reverse=-1):
    print(name)