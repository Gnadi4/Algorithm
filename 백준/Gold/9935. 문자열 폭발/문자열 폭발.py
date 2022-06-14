import sys
from collections import deque
input = sys.stdin.readline

s = input().rstrip()
comp = input().rstrip()
q = []
i = 0
while True:
    if i>=len(s): break
    if len(q) >= len(comp) and ''.join(q[len(q)-len(comp):]) == comp:
        for j in range(len(comp)):
            q.pop()
    else:
        q.append(s[i])
        i+=1
if len(q) >= len(comp) and ''.join(q[len(q)-len(comp):]) == comp:
    for j in range(len(comp)):
        q.pop()

if q:
    print(''.join(q))
else:
    print("FRULA")