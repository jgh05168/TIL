arr = [i for i in range(1, 4)]
path = [0] * 3

def backtracking(cnt):
    # 기저 조건이 가장 중요하다.
    if cnt >= 3:
        print(*path)
        return

    for num in arr:
        # 가지치기
        # 조건을 작성하는 것이 핵심
        if num in path:
            continue
    
        # 1. 재귀함수 들어가기 전 로직 - 경로 저장
        path[cnt] = num
        # 2. 다음 재귀 함수 호출
        backtracking(cnt + 1)
        # 3. 돌아와서 할 로직
        path[cnt] = 0


backtracking(0)