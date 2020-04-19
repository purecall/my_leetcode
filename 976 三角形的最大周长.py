#
# @lc app=leetcode.cn id=976 lang=python3
#
# [976] 三角形的最大周长
#

# @lc code=start


class Solution:
    # 先排序，再贪心的取最大的三个即可，判断是否能成三角形
    def largestPerimeter(self, A: List[int]) -> int:
        A.sort(reverse=True)
        for i in range(len(A)-2):
            if A[i+1]+A[i+2] > A[i]:
                return A[i]+A[i+1]+A[i+2]
        return 0
# @lc code=end
