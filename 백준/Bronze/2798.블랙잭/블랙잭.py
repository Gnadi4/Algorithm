def main():
    ans = [0]
    n,m = map(int,input().split())
    list_n = list(map(int,input().split()))

    def func(list_tmp, ind):
        if len(list_tmp)==3:
            tmp_sum = sum(list_tmp)
            if tmp_sum<=m:
                ans[0] = max(ans[0], tmp_sum)
        else:
            for i in range(ind, n):
                list_tmp.append(list_n[i])
                func(list_tmp, i+1)
                list_tmp.pop()
        
    func([], 0)

    return ans[0]

print(main())