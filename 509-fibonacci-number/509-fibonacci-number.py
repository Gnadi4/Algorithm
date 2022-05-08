class Solution:
    def fib(self, n: int) -> int:
        f = [0]*(n+1)
        if n > 0: f[1] = 1
        def fb(n):
            if n == 1 or n == 0:
                return n
            if f[n] != 0:
                return f[n]
            f[n] = fb(n-2) + fb(n-1)
            return f[n]
        return fb(n)