def shufle(deck, order):
    new_deck = [0 for _ in range(len(deck))]
    for idx, o in enumerate(order):
        new_deck[o] = deck[idx]
    return new_deck

def check(deck, order):
    idx = 0
    while idx < len(deck):
        card = deck[idx]
        person = idx % 3
        if person != order[card]:
            return False
        idx += 1
    return True

N = int(input())
P = list(map(int, input().split()))
S = list(map(int, input().split()))
deck = [i for i in range(N)]
history = set()
pw = ""
answer = 0
while True:
    if pw in history:
        answer = -1
        break
    else:
        history.add(pw)
    if check(deck, P):
        break
    deck = shufle(deck, S)
    answer += 1
    pw = "".join(map(str, deck))
print(answer)