class Piece:
    def __init__(self, y, x, dir, next=None, prev=None):
        self.y = y
        self.x = x
        self.dir = dir
        self.next = next
        self.prev = prev

def reverse_ll(piece):      # piece를 시작으로 하는 linked list 순서 뒤집기
    while piece:
        temp = piece.prev
        piece.prev = piece.next
        piece.next = temp
        if piece.prev == None:  # 뒤집힌 ll의 시작노드 반환
            return piece
        piece = piece.prev
        
def get_top_piece(piece):
    while piece:
        if piece.next == None:
            return piece
        piece = piece.next

N, K = map(int, input().split())
graph = list()
piece = list()
direction = [0, [0, 1], [0, -1], [-1, 0], [1, 0]]
for _ in range(N):
    temp = list(map(int, input().split()))
    for i in range(N):
        temp[i] = [temp[i], Piece(0,0,0)]   # 체스판 정보 + 해당 위치에 올라가 있는 체스 말 정보
    graph.append(temp)

for _ in range(K):
    y, x, dir = map(int, input().split())
    p = Piece(y-1, x-1, dir)
    p.prev = graph[y-1][x-1][1]
    p.prev.next = p
    piece.append(p)
    
turn = 0
while turn <= 1000:
    turn += 1
    for i, p in enumerate(piece):   # 1번 말부터 순서대로 이동
        posy, posx = p.y, p.x
        diry, dirx = direction[p.dir]
        tary, tarx = posy + diry, posx + dirx
        # 밖으로 나가거나 파랑일 경우 방향바꾸기
        if tary < 0 or tary >= N or tarx < 0 or tarx >= N or graph[tary][tarx][0] == 2:
            p.dir = 2 * (p.dir == 1) + 1 * (p.dir == 2) + 4 * (p.dir == 3) + 3 * (p.dir == 4)
            diry, dirx = direction[p.dir]
            tary, tarx = posy + diry, posx + dirx
            # 가로막히거나 파랑을 다시 만날 경우 그대로 있기
            if tary >= N or tary < 0 or tarx >= N or tarx < 0 or graph[tary][tarx][0] == 2:
                continue
        p.prev.next = None   # 움직일 말의 연결 끊기
        p.prev = None
        if graph[tary][tarx][0] == 0:   # 빈칸일 경우 그대로 이동
            bottom_piece = piece[i]
            top_piece = get_top_piece(graph[tary][tarx][1])
        if graph[tary][tarx][0] == 1:   # 빨강일 경우 순서뒤집기
            bottom_piece = reverse_ll(piece[i])
            top_piece = get_top_piece(graph[tary][tarx][1])
        bottom_piece.prev = top_piece
        top_piece.next = bottom_piece
        # 이동한 말 위에 있는 모든 말의 위치 업데이트
        current = bottom_piece
        while current:
            current.y = tary
            current.x = tarx
            current = current.next
        
        cnt = 0
        current = graph[tary][tarx][1].next
        while current:
            cnt += 1
            current = current.next
        if cnt >= 4:
            print(turn)
            exit(0)
    
print(-1)