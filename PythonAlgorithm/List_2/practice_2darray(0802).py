N = int(input())

arr = [list(map(int, input().split())) for _ in range(N)]

M = len(arr[0])

print('행 순서')
# 행 순서
for i in range(N):
    for j in range(M):
        print(arr[i][j], end=' ')
    print()


print()
print('열 순서')
# 열 순서
for j in range(M):
    for i in range(N):
        print(arr[i][j], end=' ')
    print()


print()
print('지그재그 순서')
# 지그재그
for i in range(N):
    for j in range(M):
        print(arr[i][j + (M-1 - 2*j) * (i%2)], end=' ')
    print()


print()
print('0으로 구성된 2차원 배열')
# 0으로 구성된 행렬을 만드는 법
zero_arr = [[0] * N for _ in range(N)]
print(zero_arr)


print()
print('각 행의 최댓갓')
max_v = 0
for i in range(N):
    total_row = 0
    for j in range(M):
        total_row += arr[i][j]
    if max_v < total_row:
        max_v = total_row