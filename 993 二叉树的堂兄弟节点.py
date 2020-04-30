#
# @lc app=leetcode.cn id=993 lang=python3
#
# [993] 二叉树的堂兄弟节点
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

# 递归 分别用两个dict来维护节点的depth和parent
class Solution:
    def isCousins(self, root: TreeNode, x: int, y: int) -> bool:
        parent = {}
        depth = {}

        def helper(node,par=None):
            if node:
                depth[node.val] = (1 + depth[par.val]) if par else 0
                parent[node.val] = par
                helper(node.left, node)
                helper(node.right, node)

        helper(root)
        return depth[x]==depth[y] and parent[x]!=parent[y]
# @lc code=end

