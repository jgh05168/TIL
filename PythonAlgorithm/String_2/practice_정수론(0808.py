'''
최대 공약수 GCD : Greatest Common Division
최소 공배수 LCM : Least Common Multiple
'''

# 최대공약수
# a > b

# 1. worst case
def gcd_1(a, b):
    for i in range(b, 0, -1):
        if a % i == 0 and b % i == 0:
            return i
     
        
# 2. 유클리드 호제법
# a > b
# a와 b, a를 b로 나눈 나머지 r이 있다고 할 떄 다음이 성립
# a와 b의 최대 공약수는 b와 r의 최대 공약수와 같다.
# 재귀적으로 a % b == r일 때를 표현 (gcd(a, b) == gcd(b, r))

def gcd_2(a, b):
    # 종료 조건
    if b == 0:
        return a
    
    # 재귀 호출
    else: 
        return gcd_2(b, a % b)
    

# 3. 최소공배수
# a와 b 의 곱을 a와 b의 최대공약수로 나눈 것과 동일
def lcm(a, b):
    return a * b // gcd_2(a, b)


a = 20
b = 15
# print(gcd_1(a, b))
print(gcd_2(a, b))
print(lcm(a, b))


'''
소수(prime number)
'''

# 에라토스테네스의 채

N = 1000
prime_numbers = [True] * N
prime_numbers[0], prime_numbers[1] = False, False

for i in range(2, int(N ** 0.5) + 1):
    if prime_numbers[i]:
        for j in range(i + i, N, i):
                prime_numbers[j] = False

print(prime_numbers)