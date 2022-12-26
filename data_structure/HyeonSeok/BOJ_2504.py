import  sys

temp = 1
sum = 0
sumlist = list()
stack = list()

string = input()
strlist = list(string)

def errorPrint():
    print(0)
    sys.exit()

def plusSum():
    k = 0
    for i in range(0, sum):
        k += sum
    return k

def push(q):
    if q == '(':
        stack.append(2)
    elif q == '[':
        stack.append(3)


def isSame(q):
    if q == ')':
        if stack[len(stack)-1] == 2:
            return True
        else:
            return False
    elif q == ']':
        if stack[len(stack)-1] == 3:
            return True
        else:
            return False

for i in range(0, len(strlist)):
    if strlist[i] == '(' or strlist[i] == '[':
        if len(stack) == 0:
            temp = 1
            sum = 0
        elif strlist[i-1] == ']' or strlist[i-1] == ')':
            if temp != 1:
                sum += temp
                temp = 1
        push(strlist[i])
    elif strlist[i] == ')' or strlist[i] == ']':
        if len(stack) == 0:
            errorPrint()
        elif isSame(strlist[i]):
            num = stack.pop()
            if len(stack) == 0:
                sum += temp
                sum = sum*num
                sumlist.append(sum)
                sum = 0
            else:
                temp = temp*num
        else:
            errorPrint()

if len(stack) != 0:
    errorPrint()

result = 0
for i in range(0, len(sumlist)):
    result += sumlist[i]
print(result)

