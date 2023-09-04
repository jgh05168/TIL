hex1 = "0F97A3"
hex2 = "01D06079861D79F99F"

def tobin(x):
    bin_string = ''
    while x != 0 and x != 1:
        bin_string += str(x % 2)
        x //= 2

    bin_string += str(x)

    return bin_string
        

def solution(hex_string):
    # hex_string : 16진수 문자열
    # 이걸 2진수 문자열로 바꾸면 길이 * 4
    l = len(hex_string) * 4

    # 16진수 문자열을 숫자로 바꾸기
    x = int(hex_string, 16)

    # 이진수로 바꾼 결과 문자열
    bin_string = tobin(x)
    while len(bin_string) != l:
        bin_string = bin_string + '0'

    bits = []
    for i in range(len(bin_string) - 1, -1, -7):
        if i < 7:
            bit = bin_string[i::-1]
            bits.append(bit)
            print(bit, end =' ')
        else:
            bit = bin_string[i:i - 7:-1]
            bits.append(bit)
            print(bit, end=' ')
    print()
    # 이진수로 만든 뒤에 이진수 출력, 그 이진수를 10진수로 바꾸고 출력
    for bit in bits:
        print(int(bit, 2), end=' ')

solution(hex1)
"""
0000111 1100101 1110100 011 
7 101 116 3
"""
print()
solution(hex2)
"""
0000000 1110100 0001100 0000111 1001100 0011000 0111010 1111001 1111100 1100111 11 
0 116 12 7 76 24 58 121 124 103 3
"""


grid = [[0] * 50000 for _ in range(50000)]

points = list(map(int, input().split()))

for i in range(0, len(points), 4):
    x, y, p, q = points[i:i + 4]
    print(x, y, p, q)