#
# @lc app=leetcode.cn id=53 lang=python3
#
# [53] 最大子序和
#

# @lc code=start
class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        dp = nums 
        # 当前最大子序和 = 当前数+前一步最大子序和 or 当前数
        for i in range(1,len(nums)):
            dp[i] = max(dp[i-1],0)+nums[i]
            
        return max(dp)
# @lc code=end

