#
# @lc app=leetcode.cn id=229 lang=python3
#
# [229] 求众数 II
#

# @lc code=start
class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        from collections import Counter
        counts = Counter(nums)
        count = len(nums) // 3

        ans = []
        for k, v in counts.items():
            if v > count:
                ans.append(k)
        return ans
# @lc code=end

