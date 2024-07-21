import sys

# 사용할 스킬의 남은 쿨타임만큼 쿨다운 후 새로운 스킬 리스트와 시간 반환
def cool_down(skill, time, cool_down_time):
    new_skill = [s[:] for s in skill]
    for s in new_skill:
        s[0] = max(0, s[0] - cool_down_time)
    time += cool_down_time
    return time, new_skill

# 스킬을 한 번씩 사용, hp를 모두 소모시키면 백트래킹
def use_skill(idx, time, hp, skill, answer):
    if hp <= 0:
        return time
    for idx, s in enumerate(skill):
        temp = s[0]
        time, new_skill = cool_down(skill, time, temp+1)
        new_skill[idx][0] = s[1]-1
        hp -= s[2]
        answer = min(answer, use_skill(idx, time, hp, new_skill, answer))
        hp += s[2]
        time -= temp+1
    return answer
    
    

N, hp = map(int, input().split())
skill = list()  # [현재 쿨타임, 스킬 쿨타임, 데미지]
time = 0
answer = sys.maxsize
for _ in range(N):
    temp = [0]
    temp.extend(list(map(int, input().split())))
    skill.append(temp)
for idx in range(N):
    temp = skill[idx][0]
    time, new_skill = cool_down(skill, time, temp+1)
    new_skill[idx][0] = skill[idx][1]-1
    hp -= skill[idx][2]
    answer = min(answer, use_skill(idx, time, hp, new_skill, answer))
    hp += skill[idx][2]
    time -= temp+1
print(answer)