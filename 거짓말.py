def have_know_man(people, know_real):
    for p in people:
        if p in know_real:
            return True
    return False

def union(parent, x, y):
    x = find(parent, x)
    y = find(parent, y)
    if y > x:
        parent[y] = x
    else:
        parent[x] = y

def find(parent, idx):
    if parent[idx] != idx:
        parent[idx] = find(parent, parent[idx])
    return parent[idx]

N, M = map(int, input().split())
know_real = list(map(int, input().split()))
know_real = set(know_real[1:])
party = list()
answer = 0
for i in range(M):
    people = list(map(int, input().split()))
    people = people[1:]
    party.append(people)
    for p in people:
        if p in know_real:
            flag = False
            break
parent = [i for i in range(len(party))]
for i in range(len(party)):
    for j in range(len(party)):
        p1 = set(party[i])
        p2 = set(party[j])
        if len(p1&p2) == 0:
            continue
        union(parent, i, j)
union_party = dict()
for idx, num in enumerate(parent):
    if num not in union_party.keys():
        union_party[num] = set()
    union_party[num] |= set(party[idx])
for key, l in union_party.items():
    if len(l&know_real) == 0:
        for p in parent:
            if p == key:
                answer += 1
print(answer)