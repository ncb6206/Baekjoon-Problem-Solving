import sys
input = sys.stdin.readline

# 테스트 케이스의 개수를 입력
t = int(input())

# 괄호 문자열이 올바른지 판단하는 함수 정의
def checkPS(string):
    temp = []
    for i in string:
        if i == '(':  # 여는 괄호일 경우
            temp.append(i)  # temp 임시 배열에 삽입
        else:  # 닫는 괄호일 경우
            if len(temp) == 0:
		            # 여는 괄호가 없으면 올바르지 않은 괄호 문자열로 판단해 False 리턴
                return False  
            temp.pop()  # 짝이 맞는 여는 괄호 제거
    
    if len(temp) == 0:  # 모든 여는 괄호가 닫혔는지 확인
        return True  # 올바른 괄호 문자열임을 확인 후 True 리턴
    else:
		    # 여는 괄호가 남아있으면 올바르지 않은 괄호 문자열이므로 False 리턴
        return False  

# 테스트 케이스에 대해 반복
array = [list(input().rstrip()) for _ in range(t)]
for test in array:
    if checkPS(test):
        print('YES')  # 올바른 괄호 문자열인 경우
    else:
        print('NO')  # 올바르지 않은 괄호 문자열인 경우