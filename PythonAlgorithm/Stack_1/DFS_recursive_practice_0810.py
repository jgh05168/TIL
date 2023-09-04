# recursive

'''
7 8
1 2
1 3
2 4
2 5
3 5
4 6
5 6
6 7
'''


# 인접리스트 생성
V, E = map(int, input().split())

adj_list = [[] for _ in range(V + 1)]
for i in range(E):
    v, e = map(int, input().split())
    adj_list[v].append(e)
    adj_list[e].append(v)
    # print(adj_list)


# 재귀로 dfs 구현 시작
visited = [False] * (V + 1)
visited[1] = True

# v : 현재 정점
def DFS_r(v):
    print(v)
    # 현재 정점에서 방문할 수 있는 정점을 찾아 방문
    for w in adj_list[v]:
        # 현재 v에서 방문할 수 있는 인접 노드들 w
        if not visited[w]:
            visited[w] = True
            DFS_r(w)        # 재귀호출

DFS_r(1)


# DFS 호출이 많이 없을 것 같을 때 재귀로 사용