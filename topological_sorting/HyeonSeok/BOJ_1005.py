from collections import deque

T = int(input())
for t in range(T):
    N, K = map(int, input().split())
    build_times = list(map(int, input().split()))
    graph = [[] for _ in range(N)]
    incount = [0 for _ in range(N)]
    for _ in range(K):
        prev, next = map(int, input().split())
        graph[prev-1].append(next-1)
        incount[next-1] += 1
    target_building = int(input()) - 1
    q = deque()
    dp = [0 for _ in range(N+1)]
    for idx, ic in enumerate(incount):
        if ic == 0:
            q.append(idx)
    while q:
        cur_building = q.popleft()
        # 현재 건물 빌드타임에 본인 짓는 시간 추가해서 dp값 완성
        dp[cur_building] += build_times[cur_building]
        # 다음단계 건물 dp 업데이트 (동시에 지을 수 있기 때문에 자식 건물중 가장 오래걸리는 시간만 남김)
        for next in graph[cur_building]:
            incount[next] -= 1
            dp[next] = max(dp[next], dp[cur_building])
            if incount[next] == 0:
                q.append(next)
        if cur_building == target_building:
            print(dp[cur_building])
            break