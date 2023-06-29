# 여우는 어떻게 울지?
import sys

T = int(sys.stdin.readline())
count = 0
answer = []
while True:
    testAnswer = []
    #print(count)
    if count == T:
        break
    sounds = list(map(str, sys.stdin.readline().split()))
    aniSound = []
    while True:
        line = sys.stdin.readline().strip()
        if line == "what does the fox say?":
            count += 1
            break
        else:
            animal = list(map(str, line.split()))
            #print("animal")
            #print(animal)
            aniSound.append(animal[2])
    #print(aniSound)

    for i in range(len(sounds)):
        if sounds[i] not in aniSound:
            testAnswer.append(sounds[i])

    answer.append(testAnswer)

for i in answer:
    for j in i:
        print(j, end=" ")
    print()
