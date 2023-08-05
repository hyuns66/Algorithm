# 폭탄 해체

import sys

numbers = ['**** ** ** ****', '  *  *  *  *  *', '***  *****  ***', '***  ****  ****', '* ** ****  *  *',
           '****  ***  ****', '****  **** ****', '***  *  *  *  *', '**** ***** ****', '**** ****  ****']

code = [[] for i in range(8)]

for i in range(5):
    line = sys.stdin.readline()
    index = 0
    count = 0
    for j in range(len(line)):
        if count == 3:
            index += 1
            count = 0
            continue

        #print("j:" + str(j) + "/i:" + str(index))
        code[index].append(line[j])
        count += 1

#print(code)

ncode = []
for i in code:
    if len(i) == 0:
        break
    flag = False
    for j in range(len(numbers)):
        test = ''.join(s for s in i)
        #print(test)
        #print(numbers[j])
        if test.strip() == numbers[j].strip():
            #print("같음")
            ncode.append(j)
            flag = True
            break
    if not flag:
        ncode.clear()
        break

#print(flag)
#print(ncode)
if len(ncode) == 0:
    print("BOOM!!")
else:
    finalCode = ''.join(str(s) for s in ncode)
    if int(finalCode) % 6 == 0:
        print("BEER!!")
    else:
        print("BOOM!!")

