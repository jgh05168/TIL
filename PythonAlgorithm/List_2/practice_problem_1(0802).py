N = int(input())

arr = [list(map(int, input().split())) for _ in range(N)]

# 방향 벡터 설정 (우 | 하 | 좌 | 상)
drow = [0, 1, 0, -1]
dcol = [1, 0, -1, 0]

sub_set = []
total_sum = 0
for row in range(N):
    for col in range(N):
        s = 0
        value = arr[row][col]
        for k in range(len(drow)):
            nrow = row + drow[k]    # 다음 행 번호 = 현재 행 번호 + 이동방향이 d일 때 변화량
            ncol = col + dcol[k]    # 다음 열 번호 = 현재 열 번호 + 이동방향이 d일 때 변화량

            # 인덱스의 범위 내에 있을 때만 명령이 수행되도록 조건 추가(내가 계산한 인덱스의 범위가 유효한지 검사)
            # 배열의 범위를 벗어나는 것을 방지
            # main 밖에 따로 isValid()함수를 사용하여 판별 가능함
            if 0 <= nrow and N > nrow and 0 <= ncol and N > ncol:
                s += abs(arr[nrow][ncol] - value)
        sub_set.append(s)
        total_sum += s

print(sub_set)
print(f'총 합 : {total_sum}')