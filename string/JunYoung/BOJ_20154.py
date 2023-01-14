# 이 구역의 승자는 누구야?!

import sys

alphabetList = [3, 2, 1, 2, 3, 3, 3, 3, 1, 1, 3, 1, 3, 3, 1, 2, 2, 2, 1, 2, 1, 1, 2, 2, 2, 1]

userString = sys.stdin.readline().strip()
numberString = []

# 알파벳을 숫자로 변환
for i in range(0, len(userString)):
    numberString.append(alphabetList[ord(userString[i]) - ord('A')])

while True:
    if len(numberString) == 1:
        break

    temp = []
    for i in range(0, len(numberString)-1, 2):
        temp.append(numberString[i] + numberString[i + 1])
    if len(numberString) % 2 != 0:  # 홀수면
        temp.append(numberString[-1])

    numberString = temp

if numberString[0] % 2 != 0:
    print("I'm a winner!")
else:
    print("You're the winner?")
