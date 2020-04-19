#
# @lc app=leetcode.cn id=62 lang=python3
#
# [62] 不同路径
#

# @lc code=start


class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        nums = [[None for i in range(m)]for i in range(n)]  # m列n行
        for i in range(m):
            nums[0][i] = 1
        for j in range(n):
            nums[j][0] = 1
        
        # dp
        for i in range(1, n):
            for j in range(1, m):
                nums[i][j] = nums[i-1][j]+nums[i][j-1]
        return nums[-1][-1]


# @lc code=end


"""
class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        num1 = num2 = 1
        for i in range(1, n):
            num1 = num1*i
        for i in range(m, m+n-1):
            num2 = num2*i
        return num2//num1
"""
