# import sys
# from collections import deque
#
# result = 0
# def result_maker(sum):
#     global result
#     if sum > result:
#         result = sum
#
# N, M = map(int, (sys.stdin.readline().split()))     # 세로 : N     가로 : M
#
# canvas = list()
# vector = deque([1, M, -1, -M])
# tetro_set = [[0, 0, 0], [2, 3, 3], [3, 2, 3], [0, 1, 2], [0, 3, 3]]
# fuckYou_tetro = [0, 1, 3, 0]        # ㅗ 모양은 따로 처리해주기
# # tetro_1 = [0, 0, 0]
# # tetro_2 = [2, 3, 3]
# # tetro_3 = [3, 2, 3]
# # tetro_4 = [0, 1, 3, 0]      # 대각 예외처리 해줘야함 (index 2, 3)
# # tetro_5 = [0, 1, 2]
#
# for i in range(N):
#     canvas.extend(list(map(int, sys.stdin.readline().split())))     # extend : 리스트 이어붙이기
#
# result = 0
# for i in range(N*M):        # canvas 의 모든 점에 대해 탐색
#     for j in range(4):      # vector 4번 rotate 하면서 4방향 탐색
#         curpos = i
#         sum = canvas[curpos]  # 현재위치에 있는 값으로 초기화
#         for idx in range(4):        # 현재 vector에 mapping 해서 방향탐색
#             if idx == 2:
#                 curpos += vector[fuckYou_tetro[idx]]       # 이동만
#             else:
#                 if curpos%5 == 0 and vector[fuckYou_tetro[idx]] == -1:
#                     sum = 0
#                     break
#                 if curpos%5 == 4 and vector[fuckYou_tetro[idx]] == 1:
#                     sum = 0
#                     break
#                 curpos += vector[fuckYou_tetro[idx]]       # 해당위치의 값 더하기
#                 if curpos < 0 or curpos >= N*M:
#                     sum = 0
#                     break
#                 else:
#                     sum += canvas[curpos]
#         result_maker(sum)
#         vector.rotate(1)
#     for tetro in tetro_set:     # 남은 4가지 테트로미노에 대해서
#         for j in range(4):      # 4 방향 vector에 대해서
#             curpos = i
#             sum = canvas[curpos]  # 현재위치에 있는 값으로 초기화
#             for idx in range(3):
#                 if curpos % 5 == 0 and vector[tetro[idx]] == -1:
#                     sum = 0
#                     break
#                 if curpos % 5 == 4 and vector[tetro[idx]] == 1:
#                     sum = 0
#                     break
#                 curpos += vector[tetro[idx]]
#                 if curpos < 0 or curpos >= N*M:
#                     sum = 0
#                     break
#                 else:
#                     sum += canvas[curpos]
#             result_maker(sum)
#             vector.rotate(1)
#
# print(result)

# DFS 사용
import sys
N, M = map(int, (sys.stdin.readline().split()))     # 세로 : N     가로 : M

canvas = [[0 for i in range(M)]for j in range(N)]
visit = [[0 for a in range(M)]for b in range(N)]
vector = [[1, 1], [-1, 1], [-1, -1], [1, -1]]
result = 0

for i in range(N):
    canvas[i] = list(map(int, sys.stdin.readline().split()))

# def DFS(x, y):       # 정상적인 조건일 때 호출 recursion
#     # if flag == 0:
#     #     return sum
#     # else:       # 정상적인 조건인지 체크해서 호출
#     #     for i in range(4):
#     #         x+=vector[i][0]
#     #         y+=vector[i][1]
#     #         if x<0 or x>=M or y<0 or y>=N:      # indexError
#     #             continue
#     #         elif
#     global result
#     cnt = 0
#     stack = list()
#     sum = canvas[y][x]
#     # 시작점 스택에 넣기
#     stack.append(x)
#     stack.append(y)
#     cnt += 1
#     visit[y][x] = 1
#     while stack and cnt < 3:
#         y = stack.pop()
#         x = stack.pop()
#         visit[y][x] = 0
#         cnt -= 1
#         for i in range(4):
#             x_pos = x + vector[i][0]
#             y_pos = y + vector[i][1]
#             if x < 0 or x >= M or y < 0 or y >= N or visit[y_pos][x_pos] == 1:  # IndexError 혹은 이미 왔던길 되돌아가는 경우
#                 continue
#             else:   # 한칸 앞으로 나아갈 때
#                 stack.append(x) # 위에서 pop 한거 다시 push (스택 유지)
#                 stack.append(y)
#                 visit[y][x] = 1
#                 cnt += 1
#                 x = x_pos
#                 y = y_pos
#                 sum += canvas[y][x]
#                 stack.append(x) # 새로운 경로로 간 위치 push (스택 증가)
#                 stack.append(y)
#                 cnt += 1
#                 visit[y][x] = 1
#                 if cnt == 3 and result < sum:
#                     result = sum
#                 break

result = 0

def DFS(x, y, idx, sum):
    global result
    if idx == 3:
        result = max(sum, result)
    else:
        for i in range(4):
            x_pos = x+vector[i][0]
            y_pos = y+vector[i][1]
            if 0<=y<N and 0<=x<M:
                if visit[y_pos][x_pos] == 0:
                    visit[y_pos][x_pos] = 1
                    DFS(x_pos, y_pos, idx+1, sum+canvas[y_pos][x_pos])
                    visit[y_pos][x_pos] = 0

def fuck_you_tetro(x, y, sum):
    global result
    for i in range(4):
        for j in range(4):
            sum += canvas[y+vector[j][1]][x+vector[j][0]]
        sum -= canvas[]

for y in range(N):
    for x in range(M):
        visit[y][x] = 1
        DFS(x, y, 0, canvas[y][x])
        visit[y][x] = 0

print(visit)