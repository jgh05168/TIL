def find_start(N):
    for i in range(N):
        for j in range(N):
            if maze[i][j] == 2:
                return i, j

def bfs(sti, stj, N):
    visited = [[0] * N for _ in range(N)]
    queue = []
    queue.append((sti, stj))
    visited[sti][stj] = 1

    while queue:
        ti, tj = queue.pop(0)
        if maze[ti][tj] == 3:               # 목적지 도착
            return visited[ti][tj] - 2      # 지나온 칸 수를 리턴
        # 인접한 좌표 확인
        for di, dj in [[0, 1], [1, 0], [0, -1], [-1, 0]]:
            ni, nj = ti + di, tj + dj
            if 0 <= ni < N and 0 <= nj < N and maze[ni][nj] != 1 and visited[ni][nj] == 0:
                queue.append((ni, nj))
                visited[ni][nj] = visited[ti][tj] + 1

    return 0        # 목적지가 경로에 없는 경우


T = int(input())

for tc in range(1, T + 1):
    N = int(input())
    maze = [list(map(int, input())) for _ in range(N)]
    sti, stj = find_start(N)
    bfs(sti, stj, N)
    ans = bfs(sti, stj, N)
    print(f'#{tc} {ans}')