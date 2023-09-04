
def bfs(s, V):  # 시작정점 : s, 정점의 개수 : V
    # 1. visited 생성
    # 2. queue 생성
    # 3. 시작정 enqueue
    # 4. 시작점 방문표시
    visited = [0] * (V + 1)
    queue = []
    queue.append(s)
    visited[s] = 1

    while queue:    # 큐에 정점이 남아있으면    --> front != rear
        v = queue.pop(0)    # dequeue
        print(v)            # 방문한 정점에서 할 일(유동적으로 수정하자)

        # 인접한 정점 중 방문하지 않은 정점 w가 있다면
        # enqueue, visited 체크
        
        # 인접리스트
        for w in adj_l[v]:
            if not visited[w]:
                queue.append(w)                 # enqueue
                visited[w] = visited[v] + 1     # 문제에 따라 써먹을수도, 써먹지 않을 수도 있다.(그냥 쓰자)
        # # 인접행렬
        # for w in range(1, V + 1):
        #     if adj_m[t][w] == 1 and visited[w] == 0:
        #         queue.append(w)                 # enqueue
        #         visited[w] = visited[v] + 1     # 문제에 따라 써먹을수도, 써먹지 않을 수도 있다.(그냥 쓰자)


'''
input 정보 : 
7 8
3 7 6 7 1 2 1 3 2 4 2 5 4 6 5 6 
'''
V, E = map(int, input().split())

arr = list(map(int, input().split()))

# 인접리스트로
adj_l = [[] for _ in range(V + 1)]
for i in range(E):
    v1, v2 = arr[i * 2], arr[i * 2 + 1]
    adj_l[v1].append(v2)
    adj_l[v2].append(v1)

# # 인접행렬로
# adj_m = [[0] * (V + 1) for _ in range(V + 1)]
# for i in range(E):
#     v1, v2 = arr[i * 2], arr[i * 2 + 1]
#     adj_m[v1][v2] = 1
#     adj_m[v2][v1] = 1

print(adj_l)
bfs(1, V)