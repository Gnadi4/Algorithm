import sys
from itertools import permutations, combinations_with_replacement
input = sys.stdin.readline

n,m = map(int, input().rstrip().split())
list_n = list(map(int, input().rstrip().split()))
list_com = combinations_with_replacement(list_n, m)
list_ans = []
chk = []
for i in list_com:
    tmp = sorted(i)
    if tmp not in chk:
        chk.append(tmp)
        list_ans.append(tmp)

list_ans = sorted(list_ans)

for i in list_ans:
    for j in i:
        print(j, end=' ')
    print()