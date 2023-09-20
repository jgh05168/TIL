'''

'''
p = [0] * 7
rank = [0] * 7

#### 1. 집합 초기화
def make_set(x):
    # 집합을 처음 만들 때는 집합에 속한 사람이 1명, 동시에 자기 자신이 대표
    p[x] = x
    rank[x] = 0



#### 2. x가 속한 집합의 대표를 얻는 연산(재귀)
def find_set(x):
    # 자기 자신의 부모가 자기 자신을 기리키고 있지 않다면, 부모를 찾아가기
    if x != p[x]:
        p[x] = find_set(p[x])
    return p[x]


def find_set2(x):   # (반복문)
    # 자기 자신의 부모가 자기 자신을 기리키고 있지 않다면, 부모를 찾아가기
    while x != p[x]:
        x = p[x]
    return p[x]


    
#### 3. 두 집합을 합치는 연산
# x가 속한 집합의 대표와 y가 속한 집합의 대표 둘 중에 하나로 대표 통일
def union(x, y):
    link(find_set(x), find_set(y))

# 3-1 rank를 나타내주는 리스트
# 트리의 깊이가 더 큰 쪽이 대표가 된다.
def link(x, y):
    # x집합의 깊이가 y집합의 깊이보다 크니까 대표를 x로
    if rank[x] > rank[y]:
        p[y] = x
    # 그게 아니면 일단 대표를 y로
    else:
        p[x] = y
        # 만약 두 집합의 깊이가 같은 경우, 부모가 되는 깊이 + 1 증가
        if rank[x] == rank[y]:
            rank[y] += 1

make_set(1)
make_set(2)
make_set(3)
make_set(4)
make_set(5)
make_set(6)

union(1, 3)
union(2, 3)
union(4, 5)
union(5, 6)
union(1, 5)
print(p)
find_set(1)         # find_set을 한번이라도 해야만 경로압축이 일어난다.
print(p)
print(rank)