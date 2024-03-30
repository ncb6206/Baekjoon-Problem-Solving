import sys
from collections import Counter
input = sys.stdin.readline

name = input().rstrip()
check = Counter(name)
count = 0
result = ""
mid = ""

for k,v in list(check.items()):
    if v % 2 == 1:
        count += 1
        mid = k
        if count >= 2:
            print("I'm Sorry Hansoo")
            exit()

for k,v in sorted(check.items()):
    result += (k * int(v//2))

print(result + mid + result[::-1])

# answer = list(set(permutations(name,len(name))))
#
# print(list(permutations(name,len(name))))
#
# for i in answer:
#     if i == i[::-1]:
#         answers.append(''.join(i))
#
# print(answers)
#
# if answers:
#     print(sorted(answers)[0])
# else:
#     print("I'm Sorry Hansoo")
