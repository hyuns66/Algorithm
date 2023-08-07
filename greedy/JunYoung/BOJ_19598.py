# 최소 회의실 개수
import heapq
import sys

room = []
N = int(sys.stdin.readline())

# for i in range(N):
#     s, e = map(int, sys.stdin.readline().split())
#     gflag  = False
#     for r in room:  # 각 방에 대하여
#         flag = True
#         for time in r:
#             start = time[0]
#             end = time[1]
#             if (start < s < end) or (start < e < end) or (s < start < e) or (s < end < e):
#                 flag = False
#                 break
#         if flag:
#             r.append([s, e])
#             gflag = True
#             break
#
#     if not gflag:
#         room.append([[s, e]])
#
#     # for i in room:
#     #     print(i)
#     # print()
#
# print(len(room))

meetings = []
for i in range(N):
     meetings.append(list(map(int, sys.stdin.readline().split())))

meetings.sort()

rooms = []
for s,e in meetings:
     if rooms and rooms[0] <= s:
          heapq.heappop(rooms)
     heapq.heappush(rooms, e)

print(len(rooms))

# 그리디..?
