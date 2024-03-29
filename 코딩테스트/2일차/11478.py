import sys

S = sys.stdin.readline()
setS = set()

for i in range(1,len(S)+1):
    j = 0
    while j+i < len(S):
        setS.add(S[j:j+i])
        j += 1

print(len(setS))

# chatGPT를 통해 시간복잡도를 O(n^3) -> O(n^2)로 리팩토링한 코드
# import sys
#
# S = sys.stdin.readline().strip()
# setS = set()
#
# # 길이가 1인 부분 문자열을 먼저 추가
# for i in range(len(S)):
#     setS.add(S[i])
#
# # 길이가 2 이상인 부분 문자열 추가
# for i in range(len(S)):
#     for j in range(i+1, len(S)+1):
#         setS.add(S[i:j])
#
# print(len(setS))