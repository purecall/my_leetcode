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



# 迭代->层次遍历，用info_dict存储每个node.val的parent和depth信息
class Solution1:
    def isCousins(self, root: TreeNode, x: int, y: int) -> bool:
        helper = [root]
        info_dict = { root.val: (None,0) }
        depth = 1
        while helper:
            new_helper = []
            for node in helper:
                if node.left:
                    info_dict[node.left.val] = (node, depth)
                    new_helper.append(node.left)
                if node.right:
                    info_dict[node.right.val] = (node, depth)
                    new_helper.append(node.right)
            helper = new_helper
            depth += 1

        return info_dict[x][0] != info_dict[y][0] and info_dict[x][1] == info_dict[y][1]