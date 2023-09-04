def funfun(n):
    '''
    1. 종료 조건 생각
    2. 재귀 호출
    '''

    if n == 0:
        print('End')
        return
    else:
        print(n)
        funfun(n - 1)
        print(n)


funfun(10)