C = int(input())

for _ in range(C):
    person = 0
    array = list(map(int,input().split()))
    N = array[0]
    middle = sum(array[1:N+1])/N

    for i in array[1:N+1]:
        if(i>middle):
            person += 1

    # 소수점이 나오게 하는 함수 round, format
    # round의 경우 57.143%와 같은 숫자는 소수 셋째짜리까지 잘나오지만 40.000%가 40.0%로 계속 출력되는 현상이 있었음.
    # format을 사용하면 40.0%가 아닌 40.000%로 소수 셋째짜리까지 제대로 출력되어서 나옴
    # round 함수 사용 예 : round(person/N*100,3)
    # format 함수 사용 예 : format(person/N*100,'.3f')
    print(f"{format(person/N*100,'.3f')}%")