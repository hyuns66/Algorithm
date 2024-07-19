import math

test_case = int(input())
answer = list()
for t in range(test_case):
    startx, starty, destx, desty = map(int, input().split())
    n = int(input())
    planets = list()
    for _ in range(n):
        planets.append(list(map(int, input().split())))

    a = 0
    for p in planets:
        px, py, psize = p
        start_is_in = True if math.sqrt((px-startx)**2 + (py-starty)**2) < psize else False
        dest_is_in = True if math.sqrt((destx-px)**2 + (desty-py)**2) < psize else False
        if start_is_in != dest_is_in:
            a += 1
            
    answer.append(a)
for a in answer:
    print(a)