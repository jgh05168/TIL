# 내가 갈 수 있는 경로 중 누적거리가 제일 짧은 것부터 고르기
import heapq

# 2. 우선순위 큐
def dijkstra(start):
    pq = []
    heapq.heappush(pq, (0, start))      # 출발점 초기화
    distance[start] = 0                 # 출발 누적거리 = 0

    while pq:
        # 현재 시점에서 누적 거리가 가장 짧은 노드에 대한 정보 꺼내기
        w, u = heapq.heappop(pq)

        # 이미 방문한 지점 + 누적 거리가 더 짧게 방문한 적이 있다면 pass
        if distance[u] < w:
            continue

        # 인접 노드를 확인
        for v_info in graph[u]:
            v = v_info[0]
            cost = v_info[1]

            new_cost = w + cost

            if distance[v] > new_cost:
                distance[v] = new_cost
                heapq.heappush(pq, (new_cost, v))
                

n, m = map(int, input().split())
# 인접리스트
graph = [[] * n]
for _ in range(m):
    u, v, w = map(int, input().split())
    graph[u].append((v, w))


# 1. 누적 거리를 계속 저장
INF = int(1e9)
distance = [INF] * n    # 초기 distance는 매우 큰 값으로 초기화

start = 0


