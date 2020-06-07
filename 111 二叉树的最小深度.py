#
# @lc app=leetcode.cn id=111 lang=python3
#
# [111] 二叉树的最小深度
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


class Solution:
    def minDepth(self, root: TreeNode) -> int:
        if not root: 
            return 0
        left = self.minDepth(root.left)
        right = self.minDepth(root.right)

        # 有为空的情况
        if not left or not right:
            return left+right+1
        # 无空的情况
        return min(left, right) + 1

# @lc code=end
