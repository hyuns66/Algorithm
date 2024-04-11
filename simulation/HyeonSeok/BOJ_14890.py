N, L = map(int, input().split())
tc_col = [[] for _ in range(N)]     # 세로로 갈 수 있는 길
test_case = list()      # 모든 길의 경우의 수
for i in range(N):
    temp = list(map(int, input().split()))  # 가로로 갈 수 있는 길
    for idx, tc in enumerate(tc_col):
        tc_col[idx].append(temp[idx])
    test_case.append(temp)
test_case += tc_col
answer = 0

for tc in test_case:
    position = 0
    height = tc[position]
    while position < N:
        if position == N-1:
            answer += 1
            break
        position += 1
        if abs(height-tc[position]) > 1:    # 높이차이가 1 이상 날 경우 해당 testcase 무시
            break
        if height < tc[position]:       # 1칸 올라왔을 경우
            can_go = True
            for i in range(position-1, position-L-1, -1):   # 이전의 L개 칸 확인해서 계단 가능여부 체크
                if i < 0 or tc[i] != height:
                    can_go = False
            if can_go:
                height = tc[position]
            else:
                break
        if height > tc[position]:
            can_go = True
            for i in range(position, position+L):
                if i >= N or tc[i] != tc[position]:
                    can_go = False
            if can_go:
                height = tc[position]
                for i in range(position, position+L):
                    tc[i] = tc[position-1]
                position += (L-1)
            else:
                break
            
print(answer)