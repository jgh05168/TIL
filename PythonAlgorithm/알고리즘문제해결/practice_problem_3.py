pat = {
    "001101": 0,
    "010011": 1,
    "111011": 2,
    "110001": 3,
    "100011": 4,
    "110111": 5,
    "001011": 6,
    "111101": 7,
    "011001": 8,
    "101111": 9,
}

hex1 = "0DEC"
hex2 = "0269FAC9A0"

def tobin(x):
    bin_string = ''
    while x != 0 and x != 1:
        bin_string += str(x % 2)
        x //= 2

    bin_string += str(x)

    return bin_string

def find_pattern(hex_string):
    # hex_string 은 16진수 문자열
    # 이진수 문자열로 바꾸면 길이가 4배
    l = len(hex_string) * 4
    x = int(hex_string, 16)  # 숫자로 바꾸기

    # 숫자를 다시 이진수 문자열로 바꾸기
    bin_string = tobin(x)
    while len(bin_string) != l:
        bin_string = bin_string + '0'

    # 뒤에서부터 검사 해서 1을 만나면 암호 해독 시작
    # 1을 만난 순간부터 6개씩 잘라서 검사
    startidx = l - 1
    for i in range(l):
        if bin_string[i] == '1':
            startidx = i
            break
    codes = []
    for i in range(startidx, l, 6):
        if l - i < 6:
            break
        else:
            bit = bin_string[i:i + 6]
            bit = bit[6::-1]
            codes.append(bit)

    
    for i in range(len(codes) - 1, -1, -1):
        if codes[i] in pat.keys():
            print(pat[codes[i]], end = ' ')    

find_pattern(hex1)
print()
find_pattern(hex2)