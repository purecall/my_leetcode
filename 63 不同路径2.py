#
# @lc app=leetcode.cn id=63 lang=python3
#
# [63] 不同路径 II
#

# @lc code=start

# 动态规划
class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        m = len(obstacleGrid)
        n = len(obstacleGrid[0])
        # m行n列
        dp = [[0]*n for _ in range(m)]

        # 初始化，把obstacleGrid对应到dp
        for i in range(m):
            if obstacleGrid[i][0] == 1:
                break
            else:
                dp[i][0] = 1

        for i in range(n):
            if obstacleGrid[0][i] == 1:
                break
            else:
                dp[0][i] = 1

        for i in range(1, m):
            for j in range(1, n):
                # 障碍物，则把dp[i][j]设置为0
                if obstacleGrid[i][j] == 1:
                    dp[i][j] = 0
                # 否则，为上边的格子+左边的格子
                else:
                    dp[i][j] = dp[i-1][j]+dp[i][j-1]
        return dp[-1][-1]

# @lc code=end
