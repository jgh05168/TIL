'''
7
9 4 9 12 4 3 4 6 12 15 15 13 15 17
'''


cleft = [0] * 20
cright = [0] * 20

E = int(input())
tree = list(map(int, input().split()))

for i in range(E):
    p, c = tree[i * 2], tree[i * 2 + 1]
    if p < c:
        cright[p] = c
    else:
        cleft[p] = c



# 이진트리 탐색 1 (재귀)
def search1(node, key):
    # 탐색하고자 하는 노드가 없다면
    if not node:
        return
    
    # 노드를 찾은 경우
    if key == node:
        print(f'Find !! ({node})')
        return node
    elif key > node:
        print('right', node, cright[node])
        return search1(cright[node], key)
    else:
        print('left', node, cleft[node])
        return search1(cleft[node], key)
    
    
# 이진트리 탐색 2 (반복문)
def search2(node, key):
    while node:
        if key == node:
            print(f'find !! ({node})')
            return node
        elif key > node:
            print('right', node, cright[node])
            node = cright[node]
        else:
            print('left', node, cleft[node])
            node = cleft[node]

    # 키를 찾지 못했다면
    return    