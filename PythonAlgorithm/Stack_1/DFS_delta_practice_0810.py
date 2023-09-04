# 미로찾기에서 사용되는 dfs

#     상 하  좌  우
dr = [-1, 1, 0, -0]
dc = [0, 0, -1, 1]

# 0이 이동할 수 있는 칸
# 1이 이동할 수 없는 벽
# 3은 도착지점
arr = [[0, 0, 0, 0, 1, 3],
       [1, 1, 0, 0, 1, 0],
       [0, 0, 0, 0, 1, 0],
       [0, 1, 0, 0, 1, 0], 
       [0, 1, 0, 0, 1, 0],
       [0, 0, 0, 0, 0, 0]]


# dfs로 2차원 배열 순회하기
# 인접한 정점 == 상하좌우

'''시작 행 번호 : r
시작 열 번호 : c
한 변의 길이 : n
'''

def dfs(r, c, n):
    visited = [[False] * n for _ in range(n)]
    stack = []

    visited[r][c] = True

    while True:
        # 현재 위치 확인해보기
        for i in range(n):
            for j in range(n):
                if (i, j) == (r, c):
                    print("*", end=' ')
                else:
                    print(arr[i][j], end=' ')
            print()
        print("==================")

        # 현재 위치가 도착점인지 확인
        if arr[r][c] == 3:
            print('도착!')
            break

        # 현재 위치(r, c)에서 다음 위치로 갈 수 있는지 확인
        # 상하좌우로 움직일 수 있는지 확인
        for d in range(len(dr)):
            nr = r + dr[d]
            nc = c + dc[d]
            # 계산 후에 (nr, nc)가 갈 수 있는 곳인지 확인
            if 0 <= nr < n and 0 <= nc < n and not visited[nr][nc] and arr[nr][nc] != 1:
                stack.append((r, c))    # row, col 정보를 튜플형식으로 저장
                # 방문 체크
                visited[nr][nc] = True
                r, c = nr, nc  
                break
        else:
            if stack:
                r, c = stack.pop()
            else:
                break



dfs(0, 0, 6)