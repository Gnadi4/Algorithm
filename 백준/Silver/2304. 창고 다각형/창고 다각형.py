import sys

input = sys.stdin.readline

n = int(input().rstrip())

list_n = [0] * 1001
max_a = 0
min_a = 1001

for _ in range(n):
    a,b = map(int, input().rstrip().split())
    list_n[a] = b
    max_a = max(a, max_a)
    min_a = min(a, min_a)

list_l = [0]
list_r = [0]

for i in range(max_a - min_a + 1):
    list_l.append(max(list_l[-1], list_n[i + min_a]))
    list_r.append(max(list_r[-1], list_n[max_a - i]))

list_ans = []
for i in range(1, max_a - min_a + 2):
    list_ans.append(min(list_l[i], list_r[max_a - min_a + 2 - i]))

print(sum(list_ans))