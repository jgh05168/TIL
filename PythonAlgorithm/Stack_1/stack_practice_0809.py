### stack을 class로 구현
class Stack:
    def __init__(self):
        self.data = []

    def push(self, item):
        self.data.append(item)
    
    def pop(self):
        if self.isEmpty():
            return "Empty"
        else:
            return self.data.pop()

    def peak(self):
        if self.isEmpty():
            return "Empty"
        else:
            return self.data[-1]
        
    def isEmpty(self):
        return len(self.data) == 0
    
stack = Stack()
stack.push(1)
stack.push(2)
print(stack.pop())
print(stack.pop())
print(stack.pop())



### stack을 인덱스로 구현(c 기반 언어에서 사용하는 방식)

top = -1
size = 10
stack = [0] * size

def push(item):
    global top
    top += 1
    if top == size:
        print("Full")
        top -= 1
    else:
        stack[top] = item


def pop():
    global top
    # print(stack, top)
    if top == -1:
        return "Empty"
    else:
        top -= 1
        return stack[top + 1]    

for i in range(15):
    push(i)

for i in range(10):
    print(pop())
