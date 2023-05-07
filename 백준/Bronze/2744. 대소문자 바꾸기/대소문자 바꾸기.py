s = input()
tmp = ''
for i in range(len(s)):
    if s[i].isupper():
        tmp += s[i].lower()
    else:
        tmp += s[i].upper()
print(tmp)