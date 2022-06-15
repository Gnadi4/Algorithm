import sys
from itertools import combinations
input = sys.stdin.readline

n,m = map(int, input().rstrip().split())
list_m = list(input().rstrip().split())

list_val = list(combinations(list_m, n))
list_ans = []
for i in list_val:
    ja = 0
    mo = 0
    for j in i:
        if j in {'a','e','i','o','u'}:
            mo += 1
        else:
            ja += 1
    if ja>=2 and mo>=1:
        s = list(i)
        list_ans.append(sorted(s))
list_ans.sort()
for i in list_ans:
    print(''.join(i))