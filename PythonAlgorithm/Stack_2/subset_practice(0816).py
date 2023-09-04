numbers = [1, 2, 3, 4, 5]
n = len(numbers)
selected = [0] * n
x = 6

# i번째 원소를 선택 or 선택하지 않았던 상황에서의 합을 기억하자
def subset(i, n, subsum):
    # 0. 다른 조건(최적화)
    if subsum > x:
        return

    # 1. 종료 조건 :  n개의 원소에 대한 모든 선택을 끝냄
    if i == n:
        temp = 0
        for j in range(n):
            if selected[j]:
                temp += numbers[j]

        # 합이 x 이하인 부분집합들만 출력
        if temp <= x:
            for j in range(n):
                if selected[j]:
                    print(numbers[j], end=' ')
            print()
        return

    # 2. 재귀 호출
    else:
        selected[i] = 1
        # i번째 원소를 선택하고 다음 i + 1 번째 원소를 선택
        subset(i + 1, n, subsum + numbers[i])
        selected[i] = 0
        # i번째 원소를 선택하지 않고 다음 i + 1 번째 원소를 선택
        subset(i + 1, n, subsum)


subset(0, n, 0)