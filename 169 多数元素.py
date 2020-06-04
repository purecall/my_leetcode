#
# @lc app=leetcode.cn id=169 lang=python3
#
# [169] 多数元素
#

# @lc code=start
# 摩尔投票法
class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        cand_num = nums[0]
        count = 1
        for i in range(1, len(nums)):
            if cand_num == nums[i]:
                count += 1
            else:
                count -= 1
                if count == 0:
                    cand_num = nums[i]
                    count = 1
        return cand_num
# @lc code=end

# collections.Counter
class Solution1:
    def majorityElement(self, nums: List[int]) -> int:
        from collections import Counter
        counts = Counter(nums)
        return max(counts.keys(), key=counts.get)

# 排序，取中间的数
class Solution2:
    def majorityElement(self, nums: List[int]) -> int:
        nums.sort()
        return nums[len(nums)//2]