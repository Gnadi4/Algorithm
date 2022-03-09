import re
import sys
input = sys.stdin.readline

test = int(input().rstrip())

for _ in range(test):
    p = input().rstrip()
    n = int(input().rstrip())
    tmp = input().rstrip()
    val = re.findall(r'\d+', tmp)
    cnt = 0
    chk = True
    for i in p:
        if not chk: break
        if i == 'R':
            cnt+=1
        else:
            if val:
                if cnt%2==0: val.pop(0)
                else: val.pop()
            else:
                chk = False
    if chk: 
        print('[', end='')
        if cnt%2==1: val = val[::-1]
        for i in range(len(val)):
            if i != len(val)-1:
                print(val[i],end='')
                print(',',end='')
            else:
                print(val[i],end='')
        print(']')
    else:
        print('error')
