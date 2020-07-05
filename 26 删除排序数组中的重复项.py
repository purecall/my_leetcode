#
# @lc app=leetcode.cn id=26 lang=python3
#
# [26] 删除排序数组中的重复项
#

# @lc code=start


class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        if len(nums) < 2:
            return len(nums)

        pre, cur = 0, 1

        while cur < len(nums):
            if nums[cur] != nums[pre]:
                nums[pre+1] = nums[cur]
                pre += 1
            cur += 1
        
        return pre + 1
            # @lc code=end
