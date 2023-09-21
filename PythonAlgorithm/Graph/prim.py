'''
7 11
0 1 32
0 2 31
0 5 60
0 6 51
1 2 21
2 4 46
2 6 25
3 4 34
3 5 18
4 5 40
4 6 51
'''

import heapq

def prim(start):
    heap = []
    # MST에 ㅍ함되었는지 여부
    mst = [0] * V       # visited 배열과 같은 역할을 한다.

    # (초기 가중치, 출발 정점) 저장
    heapq.heappush(heap, (0, start))

    weight_sum = 0

    while heap:
        # 가장 적은 가중치를 가진 정점을 꺼냄
        weight, v = heapq.heappop(heap)

        # 이미 방문한 정점이라면, pass
        if mst[v]:
            continue
        
        # 방문 체크
        mst[v] = 1

        # 가중치 누적합
        weight_sum += weight

        for next in range(V):
            # 갈 수 없거나 이미 방문했다면 pass
            if not graph[v][next] or mst[next]:
                continue
            
            heapq.heappush(heap, (graph[v][next], next))

    return weight_sum

V, E = map(int, input().split())
# 인접 행렬
graph = [[0] * V for _ in range(V)]

for i in range(E):
    v, u, w = map(int, input().split())
    # 무방향 그래프
    graph[v][u] = w
    graph[u][v] = w


# 가중치의 합 출력
print(prim(0))