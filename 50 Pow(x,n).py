#
# @lc app=leetcode.cn id=50 lang=python3
#
# [50] Pow(x, n)
#

# @lc code=start

class Solution:
    from functools import lru_cache 
    def myPow(self, x: float, n: int) -> float:
        # 考虑好负数情况
        if n < 0:
            return 1/self.helper(x, -n)
        return self.helper(x, n)

    @lru_cache
    def helper(self, x, n):
        # 分治思想
        if n == 0: # 边界情况
            return 1
        if n % 2 == 0:  # 如果是偶数
            return self.helper(x*x, n//2)
        return self.helper(x*x, (n-1)//2)*x
        # @lc code=end
