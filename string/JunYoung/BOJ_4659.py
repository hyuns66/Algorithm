# 비밀 번호 발음하기

import sys

userInput = ""
answerList = []
while True:
    userInput = sys.stdin.readline().strip()
    if userInput == "end":
        break

    acceptableFlag = False
    vowels = 0
    vowelsContinue = 1
    consonantsContinue = 1

    for i in range(0, len(userInput)):

        if userInput[i] in 'aeiou':  # 모음일때
            vowels += 1
            if i != 0:
                if userInput[i - 1] == userInput[i]:
                    if userInput[i] not in 'eo':  # ee와 oo는 예외
                        break

                if userInput[i - 1] in 'aeiou':
                    vowelsContinue += 1
                else:
                    vowelsContinue = 1

        else:  # 자음일때
            if i != 0:
                if userInput[i - 1] == userInput[i]:
                    break
                if userInput[i - 1] not in 'aeiou':
                    consonantsContinue += 1
                else:
                    consonantsContinue = 1

        if (vowelsContinue >= 3) | (consonantsContinue >= 3):  # 모음이 3개 혹은 자음이 3개 연속으로 오면 안 된다.
            break

        if (i == len(userInput) - 1) & (vowels != 0):  # 마지막까지 무사히 오면
            acceptableFlag = True

    if acceptableFlag:
        answerList.append(f"<{userInput}> is acceptable.")
    else:
        answerList.append(f"<{userInput}> is not acceptable.")

for i in range(0, len(answerList)):
    print(answerList[i])
