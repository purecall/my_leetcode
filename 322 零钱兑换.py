#
# @lc app=leetcode.cn id=322 lang=python3
#
# [322] 零钱兑换
#

# @lc code=start
class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        dp = [float("inf") for i in range(amount+1)] # 初始化dp数组
        dp[0] = 0 # 当amount==0时，硬币所需数为0

        # 举个例子 dp[10]= min(dp[10-5], dp[10-8], dp[10-1]) + 1
        for i in range(1,amount+1):
            for coin in coins:
                if i - coin >= 0:
                    dp[i] = min(dp[i], dp[i-coin]+1)
        if dp[-1]==float("inf"):
            return -1
        else:
            return dp[-1]
        
# @lc code=end

