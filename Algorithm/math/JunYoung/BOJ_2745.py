# 진법 변환

import sys

userInput = sys.stdin.readline().split()

N = userInput[0]
B = int(userInput[1])

decimalNum = 0

for i in range(0, len(N)):  # range('A', 'Z')는 안된다.
    placeValue = 0
    if ord(N[i]) in range(ord('A'), ord('Z') + 1):  # ord: 문자에 해당하는 유니코드 정수를 반환
        placeValue = ord(N[i]) - ord('A') + 10
    else:
        placeValue = int(N[i])

    decimalNum += placeValue * (B ** (len(N)-1-i))  # C언어 pow가 파이썬에선 **


print(decimalNum)

# 공백 끊어서 입력받는 법
# https://velog.io/@tbnsok40/%ED%8C%8C%EC%9D%B4%EC%8D%AC-%EB%8B%A4%EC%96%91%ED%95%9C-%EC%9E%85%EB%A0%A5%EB%B0%A9%EB%B2%95-input-read-readline

# 문자열 인덱싱
# https://aenam00.tistory.com/49

# for (i=0;i<10; i++)
# 이랑 for i in range(1,10) 이랑 같나봐.

# 실수1: 문자열 indexing은 앞에서부터 해놓고, B의 몇승은 뒤에서부터 했다.
# 실수2: B ** (len(N)-1-i) 괄호를 안쳐서 계산이 잘못됐다.