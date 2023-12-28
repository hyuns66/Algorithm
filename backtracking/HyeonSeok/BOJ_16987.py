import sys

def backTracking(position):
    global N, eggs, answer
    if position == N:
            cnt = 0
            for egg in eggs:
                if egg['shield'] <= 0:
                    cnt += 1
            answer = max(cnt, answer)
            return
    if eggs[position]['shield'] <= 0:
        backTracking(position+1)
        return
    flag = N-1
    for t in range(N):
        if eggs[t]['shield'] <= 0:
            flag -= 1
            continue
        if t == position:
            continue
        eggs[position]['shield'] -= eggs[t]['weight']
        eggs[t]['shield'] -= eggs[position]['weight']
        backTracking(position+1)
        eggs[position]['shield'] += eggs[t]['weight']
        eggs[t]['shield'] += eggs[position]['weight']
    if flag == 0:   # 모든 계란이 깨져있는 경우
        backTracking(N)

N = int(sys.stdin.readline())
eggs = [dict() for i in range(N)]
for i in range(N):
    shield, weight = map(int, sys.stdin.readline().split())
    eggs[i]['shield'] = shield
    eggs[i]['weight'] = weight
answer = 0

backTracking(0)
    
print(answer)