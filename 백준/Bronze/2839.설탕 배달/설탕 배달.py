def main():
    n = int(input())

    tmp = n//3

    for i in range(tmp+1):
        if (n-3*i)%5==0:
            return i+((n-3*i)//5)
    return -1

print(main())