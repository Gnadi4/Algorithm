import sys

input = sys.stdin.readline

n = input().rstrip()

list_n = [0]*10

for i in n:
    list_n[int(i)] += 1
val = list_n[6]+list_n[9]
list_n[6] = val//2 + val%2
list_n[9] = val//2
print(max(list_n))