# 폰 호석만

import sys

aNum, bNum = map(str, sys.stdin.readline().split())

def toDecimalNum(RandomDigitNum):
    maximum = '\0'
    digit = 0
    dictionary = {}
    for i in range(0, len(RandomDigitNum)):
        if RandomDigitNum[i] > maximum:
            maximum = RandomDigitNum[i]

    if maximum.isalpha():
        digit = ord(maximum) - ord('a') + 11
    else:
        digit = int(maximum) + 1

    # RandomDigitNum는 적어도 digit 진법 이상이다.
    for i in range(digit, 37):  #
        decimal = 0
        # RandomDigitNum 10진법으로 바꾸기
        for j in range(0, len(RandomDigitNum)):  # j가 자릿수, i가 진법
            if str(RandomDigitNum[j]).isalpha():  # 'a'~'z'인 경우
                decimal += (i ** j) * (ord(RandomDigitNum[len(RandomDigitNum) - 1 - j]) - ord('a') + 10)
            else:  # 숫자인 경우
                decimal += (i ** j) * int((RandomDigitNum[j]))
        if decimal in dictionary:  # 이미 decimal값이 key로 존재하는 경우 => 0..일때 밖에 없지 않나 흠
            dictionary[decimal].append(i)
        else:
            dictionary[decimal] = [i]
    return dictionary


aDict = toDecimalNum(aNum)
bDict = toDecimalNum(bNum)

# 0, 0 일때, dict으로 저장하니까.. 키가 갱신되가지고 안되네...
# key 중복 허용하는 자료형이 있나?

XList = []
for k in aDict.keys():
    if not (k >= 2 ** 63):  # X가 2^63 이상이 아닐때,
        if k in bDict:
            if (len(aDict.get(k)) > 1) | (len(bDict.get(k)) > 1): # 만족하는 경우가 2가지 이상일때
                common = list(set(aDict.get(k)).intersection(bDict.get(k)))
                for i in range (0, len(common)):
                    XList.append(common[i])
            else:
                if aDict.get(k) != bDict.get(k):  # 진법A와 진법B가 다를 때,
                    XList.append(k)

if len(XList) == 0:
    print("Impossible")
elif len(XList) > 1:
    print("Multiple")
else:
    X = XList[0]
    A = aDict.get(X)[0]
    B = bDict.get(X)[0]
    print("%d %d %d" % (X, A, B))

"""
딕셔너리: https://wikidocs.net/16#key-keys
"""
