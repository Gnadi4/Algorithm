import sys

n = int(sys.stdin.readline().rstrip())
ans = []
for i in range(n):
    ans.append(int(sys.stdin.readline().rstrip()))

ans.sort()

for i in ans:
    print(i)