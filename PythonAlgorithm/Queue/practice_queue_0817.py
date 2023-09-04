####### 선형 큐 #########

def isEmpty():
    return front == rear

def isFull():
    return rear == len(Q) - 1

def enqueue(item):
    global rear
    if isFull():
        print('Full!!')
    else:
        rear += 1
        Q[rear] = item
        print(Q)

def dequeue():
    global front
    if isEmpty():
        return 'Empty!!'
    else:
        front += 1
        return Q[front]

n = 3
Q = [0] * n
front, rear = -1, -1

# enqueue(1)
# enqueue(2)
# enqueue(3)
# enqueue(4)
# print(dequeue())
# print(dequeue())
# print(dequeue())
# print(dequeue())
# print()

####### 원형 큐 ########

def isEmptyc():
        return cfront == crear

def isFullc():
        return (crear + 1) % cn == cfront

def enqueuec(item):
    global crear
    if isFullc():
        print('Full!!')
    else:
        crear = (crear + 1) % cn
        cQ[crear] = item
        print(cQ)

def dequeuec():
    global cfront
    if isEmptyc():
        return 'Empty!!'
    else:
        cfront = (cfront + 1) % cn
        return cQ[cfront]
    
cn = 3
cQ = [0] * n
cfront, crear = 0, 0

enqueuec(1)
enqueuec(2)
enqueuec(3)
enqueuec(4)
print(dequeuec())
print(dequeuec())
print(dequeuec())
print(dequeuec())
print()

###### dequeue ######
from collections import deque
## deque 모듈을 사용하면 일반 pop(0) 보다 빠른 동작이 가능

A = deque([1, 2, 3])
print(list(A))
print(A.popleft(), list(A))
A.append(4)
print(list(A))
print(A.popleft(), list(A))