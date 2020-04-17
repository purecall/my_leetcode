#
# @lc app=leetcode.cn id=74 lang=python3
#
# [74] 搜索二维矩阵
#

# @lc code=start


class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        m = len(matrix)
        if m == 0:
            return False
        n = len(matrix[0])

        # 二分查找
        left, right = 0, m*n-1
        while left <= right:
            mid = (left+right)//2
            mid_elem = matrix[mid//n][mid % n]
            if target == mid_elem:
                return True
            elif target < mid_elem:
                right = mid-1
            else:
                left = mid+1
        return False


# @lc code=end
