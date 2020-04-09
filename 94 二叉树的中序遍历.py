#
# @lc app=leetcode.cn id=94 lang=python3
#
# [94] 二叉树的中序遍历
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


# 简单的递归方式
class Solution:
    def inorderTraversal(self, root: TreeNode) -> List[int]:
        # f = self.inorderTraversal
        # return f(root.left) + [root.val] + f(root.right) if root else []
        res = []

        def helper(root):
            if not root:
                return
            helper(root.left)
            res.append(root.val)
            helper(root.right)
        helper(root)
        return res

# @lc code=end
