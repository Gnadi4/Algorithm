import sys
input = sys.stdin.readline

n = int(input().rstrip())
val = [0]*3
# list_n = list(map(int, input().rstrip().split()))
# val[0] = list_n[0]
# val[1] = list_n[1]
# val[2] = list_n[2]
for i in range(n):
    list_n = list(map(int, input().rstrip().split()))
    a,b,c = val[0],val[1],val[2]
    val[0] = min(b + list_n[0], c + list_n[0])
    val[1] = min(a + list_n[1], c + list_n[1])
    val[2] = min(a + list_n[2], b + list_n[2])

print(min(min(val[0],val[1]),val[2]))