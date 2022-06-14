import sys

input = sys.stdin.readline

s1 = input().rstrip()
s2 = input().rstrip()

ans = 0
list_n = [[0]*len(s1) for _ in range(len(s2))]

for i in range(len(s2)):
    for j in range(len(s1)):
        if s1[j] == s2[i]:
            if j>0 and i>0:
                list_n[i][j] = max(list_n[i-1][j-1]+1,1)
            else:
                list_n[i][j] = 1
        ans = max(ans, list_n[i][j])

print(ans)