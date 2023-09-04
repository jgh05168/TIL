# s : 시작 정점 번호
# V : 정점의 개수

def DFS_m(s, V):
    stack = []
    visited = [False] * V
    visited[s] = True       # 시작 정점 방문
    print(node[s])

    # 모든 정점을 반복할 떄 까지 반복
    while True:
        # adj_m[s][w] == 1인 경우 방문가능
        for w in range(V):
            if adj_m[s][w] == 1 and visited[w] == False:
                stack.append(s)
                print(node[w])
                s = w
                visited[s] = True
                break
        else:
            if stack:
                s = stack.pop()
            else:
                break





# 1. 인접 행렬  -> 2차원 배열

# 무방향 그래프일 경우, 대칭행렬
# 방향 그래프일 경우, 대칭이 아님
# 간선이 존재한다면 1, 없으면 0
'''
+ A B C D E F G
A 0 1 1 0 0 0 0
B 1 0 0 1 1 0 0
C 1 0 0 0 1 0 0
D 0 1 0 0 0 1 0
E 0 1 1 0 0 1 0
F 0 0 0 1 1 0 1
G 0 0 0 0 0 1 0

7 8
1 2 1 3 2 4 2 5 3 5 4 6 5 6 6 7
'''

V, E = map(int, input().split())
node = ['A', 'B', 'C', 'D', 'E', 'F', 'G']
arr = list(map(int, input().split()))
adj_m = [[0] * V for _ in range(V)]   # 빈 인접행렬 생성
print(adj_m)
for i in range(E):
    v1, v2 = arr[i * 2] - 1, arr[i * 2 + 1] - 1
    # 대칭되는 행렬을 생성한다
    adj_m[v1][v2] = 1
    adj_m[v2][v1] = 1

DFS_m(0, V)



# 2. 인접 리스트 -> 연결리스트

# adj_l[i] : i 번 정점과 연결되어있는 정점의 모음(리스트)
# ex) adj_l[A] = [B, C]


def DFS_l(s, V):
    stack = []
    visited = [False] * (V + 1)
    visited[s] = True       # 시작 정점 방문
    print(s)

    # 모든 정점을 반복할 떄 까지 반복
    while True:
        for w in adj_l[s]:
            # w는 s와 연결되어있는 정점이다.
            # w를 방문한 적이 있는지만 확인해보기
            if visited[w] == False:
                stack.append(s)
                s = w
                print(s)
                visited[s] = True
                break
        else:
            if stack:
                s = stack.pop()
            else:
                break

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

V, E = map(int, input().split())
adj_l = [[] for _ in range(V + 1)]
for i in range(E):
    v, e = map(int, input().split())
    adj_l[v].append(e)
    adj_l[e].append(v)

DFS_l(1, V)

# 1 2 4 6 5 3 7



# DFS 호출이 많을 것 같을 때 stack 방법 사용