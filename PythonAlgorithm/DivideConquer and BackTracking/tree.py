arr = [1, 2, 1, 3, 2, 4, 3, 5, 3, 6]
#     부모, 자식 순서로 저장

######### 0. 이진 트리 저장 : 일차원 배열 저장 #############


######### 1. 인접 리스트 저장 ###############
nodes_1 = [[] for _ in range(14)]
for i in range(0, len(arr), 2):
    parentNode = arr[i]
    childNode = arr[i + 1]
    nodes_1[parentNode].append(childNode)

# 자식이 더 이상 없다는 것을 표현하기 위해 None 삽입
for li in nodes_1:
    for _ in range(len(li), 2):
        li.append(None)

# 전위 순회
def preorder(nodeNumber):
    if nodeNumber == None:
        return
    print(nodeNumber, end=' ')
    preorder(nodes_1[nodeNumber][0])
    preorder(nodes_1[nodeNumber][1])


preorder(1)
print()


######### 2. 연결 리스트로 저장 ##############
class TreeNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    # 삽입 함수
    def insert(self, childNode):
        # 왼쪽 자식이 없을 경우
        if not self.left:
            self.left = childNode
            return
        
        # 오른쪽 자식이 없을 경우
        elif not self.right:
            self.right = childNode
            return
        
        return
    
    # 전위 순회
    def preorder(self):
        # self에 값이 있는 경우
        if self != None:
            print(self.value, end=' ')
            if self.left:   # 왼쪽이 있다면 왼쪽 자식 조회
                self.left.preorder()
            if self.right:  # 오른쪽이 있다면 오른쪽 자식 조회
                self.right.preorder()
    

nodes_2 = [TreeNode(i) for i in range(14)]
for i in range(0, len(arr), 2):
    parentNode = arr[i]
    childNode = arr[i + 1]
    nodes_2[parentNode].insert(nodes_2[childNode])

nodes_2[1].preorder()