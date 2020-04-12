#
# @lc app=leetcode.cn id=78 lang=python3
#
# [78] 子集
#

# @lc code=start


class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        output = [[]]

        for num in nums:
            toAppend = []
            for curr in output:
                toAppend += [curr + [num]]
            output += toAppend

        return output
# @lc code=end
