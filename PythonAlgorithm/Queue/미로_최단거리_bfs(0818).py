dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]


# 인덱스가 유효한지 판단해주는 함수
def is_valid(r, c):
    return 0 <= r < n and 0 <= c < n


# sr : 시작 행 번호
# sc : 시작 열 번호
def bfs(sr, sc):
    # 중복 체크 배열
    visited = [[0] * n for _ in range(n)]

    q = []
    q.append((sr, sc))  # 시작 위치 정보 (sr,sc)를 큐에 삽입
    visited[sr][sc] = 1

    # 탈출하는데 걸린 거리(최소)
    distance = 0
    while q:
        # 원소를 꺼내기 전에 현재 단계에서 큐안에 방문할 원소의 개수를 확인
        # 현재 단계에서 큐의 원소를 몇개까지만 확인하면 될지 직접 계산
        size = len(q)



        for _ in range(size):
            r, c = q.pop(0)  # 현재 방문하는 위치 r,c

            # # 이동하는 과정 출력
            # for i in range(n):
            #     for j in range(n):
            #         if (i, j) == (r, c):
            #             print("★", end=" ")
            #         else:
            #             print(visited[i][j], end=" ")
            #     print()

            # print("=================")


            # 현재 방문하는 위치가 도착점인 경우 반복 중단
            if maze[r][c] == 99:
                print(f"탈출 : {distance}")
                q = []
                break

            # 현재 위치 r,c에서 4방향 탐색
            for d in range(4):
                nr = r + dr[d]
                nc = c + dc[d]
                # 다음 위치가 유효한 인덱스인지, 벽이아님, 방문한적도 없음
                if is_valid(nr, nc) and maze[nr][nc] != 1 and not visited[nr][nc]:
                    # nr, nc 방문 처리
                    q.append((nr, nc))
                    visited[nr][nc] = visited[r][c] + 1

        distance += 1

    return distance


n = 7

maze = [[0, 0, 0, 0, 0, 0, 0],
        [0, 1, 1, 1, 1, 1, 0],
        [0, 1, 0, 1, 0, 1, 0],
        [0, 0, 0, 1, 0, 0, 0],
        [1, 0, 1, 1, 1, 0, 1],
        [1, 0, 1, 99, 0, 0, 1],
        [0, 0, 1, 1, 1, 0, 1]]

# maze = [[0, 0, 0, 0, 0, 0, 0],
#         [0, 0, 0, 0, 0, 0, 0],
#         [0, 0, 0, 0, 0, 0, 0],
#         [0, 0, 0, 1, 0, 0, 0],
#         [0, 0, 0, 0, 0, 0, 0],
#         [0, 0, 0, 0, 0, 0, 0],
#         [0, 0, 0, 0, 0, 0, 0]]

print(bfs(3, 3))
