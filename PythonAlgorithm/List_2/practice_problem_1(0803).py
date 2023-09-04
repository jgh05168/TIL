# 각 부분집합의 합이 10인 것이 존재할 경우 1 출력, 없으면 0 출력

T = int(input())

for tc in range(1, T + 1):
    arr = list(map(int, input().split()))

    n = len(arr)
    count = 0
    
    for i in range(1, (1 << n)):
        s = 0
        for j in range(n):
            if i & (1 << j):
                s += arr[j]

        if s == 0:
            count = 1
        


    print(f'#{tc} {count}')