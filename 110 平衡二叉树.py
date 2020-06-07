#
# @lc app=leetcode.cn id=110 lang=python3
#
# [110] 平衡二叉树
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


# 自顶向下，O(nlogn)
class Solution:
    def isBalanced(self, root: TreeNode) -> bool:
        if not root:
            return True
        return abs(self.depth(root.left)-self.depth(root.right)) <= 1 and \
            self.isBalanced(root.left) and self.isBalanced(root.right)

    def depth(self, root):
        if not root:
            return 0
        return max(self.depth(root.left), self.depth(root.right)) + 1
# @lc code=end


# 自底向上，O(n)
class Solution1:
    def isBalanced(self, root: TreeNode) -> bool:
        return self.recur(root) != -1

    def recur(self, root):
        # 递归终止条件
        # 叶子节点，返回高度0
        # 返回-1时，说明不是平衡树

        # 当节点root的左右子树高度差<2，
        # 返回以节点root为根节点的子树的最大高度，
        # 即max(left, right)+1

        # 当节点root的左右子树高度差>=2，
        # 则返回-1，代表此子树不是平衡树
        if not root:
            return 0

        left = self.recur(root.left)
        if left == -1:
            return -1

        right = self.recur(root.right)
        if right == -1:
            return -1

        return max(left, right) + 1 if abs(left-right) < 2 else -1