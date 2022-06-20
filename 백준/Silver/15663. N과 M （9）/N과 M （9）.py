import sys
from itertools import permutations
input = sys.stdin.readline

n,m = map(int, input().rstrip().split())
list_n = list(map(int, input().rstrip().split()))

list_com = permutations(list_n, m)
list_com = sorted(list(set(list_com)))

for i in list_com:
    for j in i:
        print(j, end=' ')
    print()