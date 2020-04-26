#
# @lc app=leetcode.cn id=152 lang=python3
#
# [152] 乘积最大子数组
#

# @lc code=start
class Solution:
    from typing import List
    def maxProduct(self, nums: List[int]) -> int:
        mi = ma = res = nums[0]
        for i in range(1, len(nums)):
            if nums[i]<0:
                mi,ma = ma,mi
            ma = max(ma*nums[i], nums[i])
            mi = min(mi*nums[i], nums[i])
            res = max(res, ma)
        return res
# @lc code=end

