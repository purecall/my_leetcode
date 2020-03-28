class Solution:
    # f(n) = f(n-1) + f(n-2)
    def climbStairs(self, n: int) -> int:
        if n <= 2:
            return n
        f1, f2, f3 = 1, 2, 3
        for _ in range(3, n+1):
            f3 = f1 + f2
            f1 = f2
            f2 = f3
        return f3