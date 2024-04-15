import sys
input = sys.stdin.readline

S = input().rstrip()        # 문자열 S 입력받기
T = input().rstrip()        # 문자열 T 입력받기

def dfs(word):
    # 문자열의 길이가 S와 같다면
    if len(S) == len(word):
        # S와 일치한다면 1 출력 후 프로그램 종료
        if word == S:
            print(1)
            exit(0)
        # S와 일치하지 않는다면 0 반환
        else:
            return 0

    # 마지막 문자가 A라면 마지막 문자를 제거하고 재귀 호출
    if word[-1] == 'A':        
        dfs(word[:-1])    
    
    # 첫 번째 문자가 B라면 문자열을 뒤집고 첫 번째 문자를 제거한 뒤 재귀 호출
    if word[0] == 'B':
        dfs(word[::-1][:-1])

dfs(T)      # T로 시작하여 깊이 우선 탐색 수행
print(0)    # 찾지 못한 경우 0 출력