import sys
input = sys.stdin.readline

N = int(input())
words = [input().rstrip() for _ in range(N)]
M = int(input())
answer = [input().rstrip() for _ in range(M)]

if words[0] == "?":
    if len(words) == 1:
        print(answer[0])
    else:
        for item in answer:
            if item[-1] == words[1][0] and item not in words:
                print(item)
                break

elif words[-1] == "?":
    for item in answer:
        if item[0] == words[-2][-1] and item not in words:
            print(item)
            break
        
else:
    for i in range(N):
        if(words[i] == '?'):
            prev = words[i-1][-1]
            next = words[i+1][0]
            
            for item in answer:
                if prev == item[0] and next == item[-1] and item not in words:
                    print(item)
                    break
        
# index = -1
# prev,next = "",""

# for i in range(N):
#     word = input().rstrip()
#     answer.append(word)
#     if word == "?":
#         index = i
    
# if index == 0:
#     next = answer[index+1]
    
# elif index == N-1:
#     prev = answer[index-1]

# else:
#     prev = answer[index-1]
#     next = answer[index+1]

# for _ in range(M):
#     word = input().rstrip()
#     if index == 0:
#         if len(answer) == 1:
#             print(word)
#             break
#         if next and next[0] == word[-1] and word not in answer:
#             print(word)
#             break
#     elif index == N-1:
#         if prev and prev[-1] == word[0] and word not in answer:
#             print(word)
#             break
#     else:
#         if prev and next and prev[-1] == word[0] and next[0] == word[-1] and word not in answer:
#             print(word)
#             break