import sys
from itertools import combinations
input = sys.stdin.readline
t = int(input().rstrip())

for _ in range(t):
    n = int(input().rstrip())
    list_n = []
    for _ in range(n):
        list_n.append(list(map(int, input().rstrip().split())))
    x_sum = sum([list_n[i][0] for i in range(n)])
    y_sum = sum([list_n[i][1] for i in range(n)])
    val = float("inf")
    r_list = list(combinations([i for i in range(n)],n//2))
    r_list = r_list[:len(r_list)//2]
    for r in r_list:
        x_val = 2 * sum([list_n[i][0] for i in r]) - x_sum
        y_val = 2 * sum([list_n[i][1] for i in r]) - y_sum
        val = min(val, (x_val**2 + y_val**2)**(0.5))
    print(val)