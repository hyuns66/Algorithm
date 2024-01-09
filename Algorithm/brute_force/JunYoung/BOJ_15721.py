#번데기
import sys

A = int(sys.stdin.readline())
T = int(sys.stdin.readline())
guhoo = int(sys.stdin.readline())

fun = []
dagii = []

round = 1
who = 0
while True:

    fun.append(who)
    who = (who+1) % A
    dagii.append(who)
    who = (who + 1) % A
    fun.append(who)
    who = (who + 1) % A
    dagii.append(who)
    who = (who + 1) % A
    for i in range(0,round+1):
        fun.append(who)
        who = (who + 1) % A
    for i in range(0,round+1):
        dagii.append(who)
        who = (who + 1) % A

    round += 1
    #print(fun)
    #print(dagii)

    if guhoo==0:
        if len(fun)>=T:
            print(fun[T-1])
            break
    else:
        if len(dagii)>=T:
            print(dagii[T-1])
            break
