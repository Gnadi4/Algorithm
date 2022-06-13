import sys

input = sys.stdin.readline

n = int(input().rstrip())

def add(x):
    list_n[x] = x

def remove(x):
    list_n[x] = 0

def check(x):
    return list_n[x] == x

def toggle(x):
    if list_n[x] == x:
        list_n[x] = 0
    else:
        list_n[x] = x

def all():
    return [i for i in range(21)]

def empty():
    return [0]*21

list_n = [0]*21

for i in range(n):
    s = input().rstrip().split()
    if s[0] == 'add':
        add(int(s[1]))
    elif s[0] == 'remove':
        remove(int(s[1]))
    elif s[0] == 'check':
        if(check(int(s[1]))):
            print(1)
        else:
            print(0)
    elif s[0] == 'toggle':
        toggle(int(s[1]))
    elif s[0] == 'all':
        list_n = all()
    elif s[0] == 'empty':
        list_n = empty()

