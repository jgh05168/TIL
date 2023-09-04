## SW문제해결 8일차 - 이진 힙

'''
1. n + 1 개 배열 생성
2. last(위치를 나타내는 변수) 초기화

'''

# 최대 힙
'''
        20
      /    \
    15      19
   / \      /  
  4   13   11
'''    


# 삽입 연산
def enq(item):
    global last
    last += 1       # 마지막 위치에 원소 추가
    heap[last] = item
    
    # 원소를 추가한 뒤 "부모노드 > 자식노드"  조건을 만족하도록 해야 한다
    # 현재 위치를 자시 ㄱ노드로 생각
    # 부모노드의 위치를 계산
    c = last
    p = c // 2
    # 부모 노드가 존재하고, 자식 노드가 부모 노드보다 작을 떄까지 위치를 바꾼다.
    while p and heap[p] < heap[c]:
        heap[p], heap[c] = heap[c], heap[p]
        # 위치를 바꾼 뒤 부모, 자식 노드 번호 업데이트
        c = p
        p = c // 2



# 삭제 연산(정럴 후 첫번째 max값 출력 시)
def deq():
    global last
    tmp = heap[1]           # 루트노드값 백업
    heap[1] = heap[last]    # 삭제할 노드의 키를 루트에 복사
    heap[last] = 0          # 마지막 노드 0으로 초기화 후,
    last -= 1               # 마지막 노드 삭제
    
    p = 1           # 루트에 옮긴 값을 자식과 비교
    c = p * 2       # 왼쪽 자식 (비교할 자식 노드의 번호)
    # 왼쪽 자식의 idx가 last보다 작아야지 트리 안에 존재하는 것임.
    while c <= last:    # 자식이 하나라도 있으면 시작
                        # 왼쪽 자식 없이 오른쪽 자식만 있을 수는 없다. -> 완전이진트리를 따르기 때문
        if c + 1 <= last and heap[c] < heap[c + 1]:      # 왼쪽도 존재, 오른쪽도 존재할 때 오른쪽 자식이 더 크다면
            c += 1      # 비교 대상이 오른쪽 자식노드가 되므로 +1 수행
        if heap[p] < heap[c]:   # 부모노드와 자식노드 비교 -> 자식노드가 값이 더 크다면,
            heap[p], heap[c] = heap[c], heap[p]     # swap
            p = c           # 자식을 새로운 부모로
            c = p * 2       # 왼쪽 자식 번호를 계산
        else:   # 부모가 더 크다면
            break
    
    return tmp

heap = [0] * (10 + 1)
last = 0
arr = [10, 6, 4, 5, 1, 3, 2, 9, 7, 8]
sorted_arr = []
# 원소 삽입
for i in range(10):
    enq(arr[i])
print(heap)     # 최대 힙이기 때문에 heap[1] == max_value
 
for i in range(10):
    sorted_arr.append(deq())
print(sorted_arr)



## 번외 - 힙 라이브러리 존재
import heapq        # 최소힙 기반
hp = []
for i in range(10, 0, -1):
    heapq.heappush(hp, i)
for i in range(10):
    print(heapq.heappop(hp), end=' ')
print()

# 응용
heapq.heappush(hp, (4, "4등"))  # 튜플의 0위치의 값 : key
heapq.heappush(hp, (1, "1등"))
heapq.heappush(hp, (3, "3등"))
heapq.heappush(hp, (2, "2등"))
for i in range(4):
    print(heapq.heappop(hp))