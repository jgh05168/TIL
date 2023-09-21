# 모든 간선들 중 비용이 가장 적은 것을 우선으로 고르기

V, E = map(int, input().split())

edge = []
for _ in range(E):
    u, v, w = map(int, input().split())
    edge.append((u, v, w))

# 비용이 가장 낮은 순으로 오름차순 정렬
edge.sort(key=lambda x: x[2])



# 사이클 발생 여부를 union-find로 해결
parents = [i for i in range(V)]

def find_set(x):
    if parents[x] != x:
        parents[x] = find_set(parents[x])
    return parents[x]

def union(x, y):
    x, y = find_set(x), find_set(y)

    # 여기서 사이클 발생
    if x == y:
        return
    if x < y:
        parents[y] = x
    else:
        parents[x] = y

# 현재 방문한 정점 수
cnt = 0
weight_sum = 0
for u, v, w in edge:
    # 사이클이 발생하지 않는다면
    if find_set(u) != find_set(v):
        cnt += 1
        weight_sum += w
        union(u, v)
        # MST가 완성되었다면
        if cnt == V:
            break

# 가중치의 합 출력
print(weight_sum)