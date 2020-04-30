#
# @lc app=leetcode.cn id=102 lang=python3
#
# [102] �������Ĳ�α���
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

# 1. 开始时，队列helper只有根节点，访问helper中的每一个节点
#    依次将节点的值保存在列表new_helper中，并将节点的左右孩子节点(如果有)加入到this_layer_result
# 2. 用new_helper替换helper，继续遍历，直到helper为空

class Solution:
    def levelOrder(self, root: TreeNode) -> List[List[int]]:
        if not root:
            return []
        helper = [root]
        result = []
        while helper:
            new_helper = []
            this_layer_result = []
            for node in helper:
                this_layer_result.append(node.val)
                if node.left:
                    new_helper.append(node.left)
                if node.right:
                    new_helper.append(node.right)
            result.append(this_layer_result)
            helper = new_helper
        return result

# @lc code=end

