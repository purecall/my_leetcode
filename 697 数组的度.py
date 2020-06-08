#
# @lc app=leetcode.cn id=697 lang=python3
#
# [697] 数组的度
#

# @lc code=start


# 一个dict当Counter用
# 记录每个元素的第一次出现的下标和最后一次出现的下标，left right
# len_num = right[num] - left[num] + 1
class Solution:
    def findShortestSubArray(self, nums: List[int]) -> int:
        count, left, right = {}, {}, {}
        for i, x in enumerate(nums):
            if x not in left:
                left[x] = i
            right[x] = i
            count[x] = count.get(x, 0) + 1

        ans = len(nums)
        max_count = max(count.values())

        for x in count:
            if count[x] == max_count:
                ans = min(ans, right[x]-left[x]+1)

        return ans
# @lc code=end
