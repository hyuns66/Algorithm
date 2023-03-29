# 오리

import sys

record = sys.stdin.readline().strip()
roomDuck = []
soundOfDuck = "quack"
notCorrect = False


def indexSound(x):
    for i in range(len(soundOfDuck)):
        if x == soundOfDuck[i]:
            return i


if record[0] == 'q':
    roomDuck.append([record[0]])
else:
    notCorrect = True

if not notCorrect:
    for s in record[1:]:
        flag = False  # 기존오리가 소리낼 수 있는지 여부 유무
        index = indexSound(s)
        if index == 0:  # q이면
            for i in range(len(roomDuck)):
                if len(roomDuck[i]) == len(soundOfDuck):
                    roomDuck[i].clear()
                    roomDuck[i].append(s)
                    flag = True
                    break
        else:  # u,a,c,k이면
            for i in range(len(roomDuck)):
                if soundOfDuck[index - 1] == roomDuck[i][-1]:
                    roomDuck[i].append(s)
                    flag = True
                    break

        if not flag: # 기존 오리가 소리를 낼 수 있는 상황이 아니면,
            if s == 'q':
                roomDuck.append([s])  # 새로운 오리추가
                #print(f"새로운 오리 추가됨 : {roomDuck}")
            else:
                notCorrect = True
                break
        #else:
        #    print(f"기존 오리(index:{i})에 {s}소리 추가됨 : {roomDuck}")


for duck in roomDuck:
    if len(duck) != len(soundOfDuck):
        notCorrect = True
        break

if notCorrect:
    print(-1)
else:
    print(len(roomDuck))
