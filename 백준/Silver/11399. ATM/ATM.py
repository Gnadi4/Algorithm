import sys
input = sys.stdin.readline

n = int(input().rstrip())
list_n = sorted(list(map(int, input().rstrip().split())))

ans = 0
for i in range(n):
    ans += sum(list_n[0:i+1])
print(ans)