#
# @lc app=leetcode.cn id=120 lang=python3
#
# [120] 三角形最小路径和
#

# @lc code=start


class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        dp = triangle
        i = len(triangle)-2 # len==4,从triangle[2]开始dp
        while i >= 0:
            # 注:[len(triangle)-2 ... 0]
            # 倒着取，即range(len(triangle)-2,-1,-1)
            # 因为range(0,3)也取不到3，这里倒过来要取到0，所以要写取不到的下一个数 -1
            for j in range(len(triangle[i])):
                dp[i][j] += min(dp[i+1][j], dp[i+1][j+1])
            i -= 1
        return dp[0][0]

# @lc code=end
