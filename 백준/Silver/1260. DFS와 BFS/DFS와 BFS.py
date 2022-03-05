import sys
from collections import defaultdict
input = sys.stdin.readline

n,m,v = map(int,input().split())
dict_val = defaultdict(list)

for i in range(m):
    a,b = map(int,input().split())
    if b not in dict_val[a]:
        dict_val[a].append(b)
        dict_val[b].append(a)

for i in dict_val:
    dict_val[i].sort()

def dfs(st, chk):

    tmp=[]
    chk += [st]
    tmp += [st]
    for i in dict_val[st]:
        if i not in chk: tmp+=dfs(i, chk)

    return tmp

def bfs(st, chk):
    
    tmp = [st]
    chk = [st]

    while chk:
        val = chk.pop(0)
        for i in dict_val[val]:
            if i not in tmp: 
                chk.append(i)
                tmp.append(i)
    return tmp

dfs_ans = []
dfs_ans += dfs(v, [])
for i in dfs_ans:
    print(i,end=' ')

print()

bfs_ans = []
bfs_ans += bfs(v, [])
for i in bfs_ans:
    print(i,end=' ')