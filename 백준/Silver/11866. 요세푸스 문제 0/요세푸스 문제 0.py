import sys
from collections import deque

input = sys.stdin.readline

n,m = map(int, input().rstrip().split())
list_n = [i+1 for i in range(n)]
q = deque(list_n)
ans = []
cnt = 1
while q:
    if cnt == m:
        cnt = 1
        ans.append(q.popleft());
    else:
        cnt += 1
        q.append(q.popleft())
print('<',end='')
for i in range(len(ans)-1):
    print(ans[i],end='')
    print(', ',end='')
print(ans[-1],end='')
print('>')