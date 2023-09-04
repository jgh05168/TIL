T = int(input())

for tc in range(1, T + 1):
    bracket = input()
    
    stack = []      # 빈 스택 생성
    for i in bracket:
        if i == '(':        # 열린 괄호일 경우, stack에 추가
            stack.append(i)
        elif i == ')':              # 닫힌 괄호일 경우
            if len(stack) == 0:     # 스택의 길이가 0인데, 닫힌 괄호가 존재한다면
                answer = False      # answer = False
                break
            stack.pop()             # break 당하지 않았으면 pop
    
        if len(stack) == 0:         # 다 돌았을 때 길이가 0이라면, True
            answer = True
    
    # 반복문이 모두 끝난 뒤 stack에 값이 존재한다면 answer = False
    if len(stack) != 0:
        answer = False
    
    print(f'#{tc} {answer}')