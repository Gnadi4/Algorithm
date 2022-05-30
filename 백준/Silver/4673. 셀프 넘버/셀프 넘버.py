list_n = [0]*10001
list_n[0] = 1

for i in range(1, 10001):
    val = i+sum(list(map(int,str(i))))
    if val <= 10000: list_n[val] = 1

for i in range(1, 10001):
    if list_n[i] == 0: print(i)