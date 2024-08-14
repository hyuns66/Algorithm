# 팀 조합 생성
def combination(N, numbers=set(), start=0):
    if len(numbers) == N // 2:
        yield numbers
        return

    for i in range(start, N):
        numbers.add(i)
        yield from combination(N, numbers, i + 1)
        numbers.remove(i)

N = int(input())
graph = list()
for _ in range(N):
    graph.append(list(map(int, input().split())))

answer = 99999999999
for link in combination(N):
    # 링크팀 점수
    link_team = list(link)
    link_score = 0
    for a in range(len(link)):
        for b in range(a+1, len(link)):
            link_score += graph[link_team[a]][link_team[b]]
            link_score += graph[link_team[b]][link_team[a]]
    # 스타트팀 점수
    start_score = 0
    for i in range(N):
        if i in link:
            continue
        for j in range(i+1, N):
            if j in link:
                continue
            start_score += graph[i][j]
            start_score += graph[j][i]
    answer = min(answer, abs(link_score - start_score))
print(answer)
