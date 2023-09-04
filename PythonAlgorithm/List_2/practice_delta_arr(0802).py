N = int(input())

arr = [list(map(int, input().split())) for _ in range(N)]


print('각 4 방향 별 합의 최댓값 구하기')
print('첫번쨰 방법')
# 각 4 방향 별 합의 최댓값 구하기
drow = [0, 1, 0, -1]
dcol = [1, 0, -1, 0]

max_v = 0   
for row in range(N):
    for col in range(N):
        # arr[row][col]을 중심으로
        s = arr[row][col]
        for k in range(len(drow)):
            nrow = row + drow[k]
            ncol = col + dcol[k]
            if nrow >= 0 and nrow < N and ncol >= 0 and ncol < N:
                s += arr[nrow][ncol]
        # 여기까지 인접 원소들의 합
        if max_v <= s:
            max_v = s

print(max_v)


# drow, dcol 배열을 미리 생성하지 않고 for문에서 정의한 경우
print('두번째 방법')
max_v = 0   
for row in range(N):
    for col in range(N):
        # arr[row][col]을 중심으로
        s = arr[row][col]
        for drow2, dcol2 in [[0, 1], [1, 0], [0, -1], [-1, 0]]:
            nrow = row + drow2
            ncol = col + dcol2
            if nrow >= 0 and nrow < N and ncol >= 0 and ncol < N:
                s += arr[nrow][ncol]
        # 여기까지 인접 원소들의 합
        if max_v <= s:
            max_v = s

print(max_v)

print()
# 몇 칸(counts) 내의 4방향 값들의 합을 구하라
2
print('몇 칸(counts) 내의 4방향 값들의 합을 구하라')
counts = int(input())

s = 0
max_v = 0   
for row in range(N):
    for col in range(N):
        # arr[row][col]을 중심으로
        s = arr[row][col]
        for c in range(counts):
            for k in range(len(drow)):
                nrow = row + drow[k] * (c+1)
                ncol = col + dcol[k] * (c+1)
                if nrow >= 0 and nrow < N and ncol >= 0 and ncol < N:
                    s += arr[nrow][ncol]
        # 여기까지 인접 원소들의 합
        if max_v <= s:
            max_v = s

print(max_v)
