# 내가 짠 코드는 아니지만 알고리즘 확인용

def count_sort(arr):
    count = {}
    for num in arr:
        if num != 0:  
            if num in count:
                count[num] += 1
            else:
                count[num] = 1
    sorted_arr = []
    for num, freq in sorted(count.items(), key=lambda x: (x[1], x[0])):
        sorted_arr.extend([num, freq])
    return sorted_arr

def r_operation(A):
    max_len = 0  
    for i in range(len(A)):
        A[i] = count_sort(A[i])  
        max_len = max(max_len, len(A[i])) 
  
    for i in range(len(A)):
        A[i] += [0] * (max_len - len(A[i]))

def c_operation(A):
    
    A[:] = list(zip(*A))
    r_operation(A)  
 
    A[:] = list(zip(*A))

def solution(r, c, k, A):
    time = 0  
  
    while time <= 100:
        
        if r <= len(A) and c <= len(A[0]) and A[r-1][c-1] == k:
            return time  
  
        if len(A) >= len(A[0]):
            r_operation(A)
        else:
            c_operation(A)
        time += 1  
    return -1 

r, c, k = map(int, input().split())
A = [list(map(int, input().split())) for _ in range(3)]

print(solution(r, c, k, A))
