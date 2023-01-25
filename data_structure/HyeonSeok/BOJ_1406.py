import sys

class CharTrain:
    def __init__(self, char, next = None):
        self.next = next
        self.char = char
        self.prev = None

    def set_next(self, target):
        self.next = target

    def set_prev(self, target):
        self.prev = target


char_set = list(sys.stdin.readline().rstrip())
num = int(sys.stdin.readline())
start = CharTrain(None)
end = CharTrain(None)
start.set_next(end)
end.set_prev(start)
curser = start

for char in char_set:
    target = CharTrain(char)
    curser.next.set_prev(target)
    target.set_next(curser.next)
    curser.set_next(target)
    target.set_prev(curser)
    curser = curser.next

for _ in range(num):
    cmd = list(sys.stdin.readline().split())
    if cmd[0] == 'L':
        if curser is not start:
            curser = curser.prev
    elif cmd[0] == 'D':
        if curser.next is not end:
            curser = curser.next
    elif cmd[0] == 'B':
        if curser is not start:
            curser.prev.next = curser.next
            temp = curser
            curser = curser.prev
            del temp
    elif cmd[0] == 'P':
        target = CharTrain(cmd[1])
        target.set_next(curser.next)
        target.set_prev(curser)
        curser.next.prev = target
        curser.next = target
        curser = curser.next

curser = start.next
while curser is not end:
    print(curser.char, end="")
    curser = curser.next