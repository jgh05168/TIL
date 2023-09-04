'''
!!!!! 무조건 그림 그려서 따라가보기 !!!!!
'''

# case 1
numbers = [1, 2, 3, 4, 5]
n = len(numbers)

# i번째 원소의 자리를 바꿔가면서 순열 생성
# 자리를 바꿀 수 있는 경우의 수
def per1(i):
    # 종료 조건
    if i == n:
        print(numbers)
        return
    
    # 재귀 호출
    # 현재 위치 i 에서 다른 위치 j에 있는 숫자와 자리를 바꾼다.
    # j를 선택할 때는 중복 방지를 위해 i보다 뒤에 있는 원소만 선택
    # i == j 인 경우도 존재(자리 swap x)
    for j in range(i, n):
        # i 번째와 j번째 위치를 바꾸고 진행
        numbers[i], numbers[j] = numbers[j], numbers[i]
        per1(i + 1)     # i + 1 원소의 자리를 바꾸기 위한 재귀호출
        # i 번째와 j번째 위치를 되돌린 뒤 다음 진행
        numbers[i], numbers[j] = numbers[j], numbers[i]
        
# per1(0)


# case 2 : 순열의 i번째 자리를 직접 선택하는 방법
# i 번째 자리를 누구로 선택했는지 기억하는 과정 필요(중복선택을 피하기 위함)

# selected[i] : i 번째 위치에 사용한 원소(selected 배열 자체가 순열)
# selected = [0] * n

def per2(i, selected):
    # 종료 조건
    if i == n:
        print(selected)
        return
    
    # 재귀 호출
    # 현재 위치 i에 누구를 놓을 것인가 선택
    # 이전에 선택했던 원소는 선택 x
    for j in range(n):
        if numbers[j] not in selected:      # 숫자 중복이 없다는 가정 하에 진행
            # i 번쨰 위치에 j 놓기
            selected[i] = numbers[j]
            # i + 1 번째 위치에 누구를 놓을지 정하는 재귀호출
            per2(i + 1, selected)
            # 다른 j를 선택하기 위한 설정
            selected[i] = 0

selected = [0] * 5
per2(0, selected)