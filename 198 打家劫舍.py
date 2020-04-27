#
# @lc app=leetcode.cn id=198 lang=python3
#
# [198] 打家劫舍
#

# @lc code=start
class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums)==0:
            return 0
        
        dp=[[0]*2 for _ in range(len(nums))]
        # 二维dp,0代表不取，1代表取
        dp[0][0] = 0
        dp[0][1] = nums[0]
        
        for i in range(1,len(nums)):
            dp[i][0] = max(dp[i-1][0],dp[i-1][1])
            dp[i][1] = dp[i-1][0] + nums[i]
        return max(dp[-1][0], dp[-1][1])
# @lc code=end

