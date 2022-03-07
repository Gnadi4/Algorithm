import sys
from collections import defaultdict
input = sys.stdin.readline

n = int(input().rstrip())
m = int(input().rstrip())

dict_val = defaultdict(list)

for _ in range(m):
    a,b = map(int, input().rstrip().split())
    dict_val[a].append(b)
    dict_val[b].append(a)

visited = []

def func(st):
    visited.append(st)
    ans = 1
    for i in dict_val[st]:
        if i not in visited:
            ans += func(i)

    return ans
res = -1
res += func(1)

print(res)