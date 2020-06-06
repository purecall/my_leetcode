#
# @lc app=leetcode.cn id=118 lang=python3
#
# [118] 杨辉三角
#

# @lc code=start


class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        nums = [[1 for _ in range(idx+1)] for idx in range(numRows)]
        for i in range(1, numRows):
            for j in range(1, i):
                nums[i][j] = nums[i-1][j-1] + nums[i-1][j]
        return nums
# @lc code=end
