#
# @lc app=leetcode.cn id=103 lang=python3
#
# [103] 二叉树的锯齿形层次遍历
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def zigzagLevelOrder(self, root: TreeNode) -> List[List[int]]:
        if not root:
            return []

        cur_nodes = [root]
        all_result = []
        flag = True
        while cur_nodes:
            new_nodes = []
            this_layer_result = []
            for node in cur_nodes:
                this_layer_result.append(node.val)
                if node.left:
                    new_nodes.append(node.left)
                if node.right:
                    new_nodes.append(node.right)
            
            if flag:
                all_result.append(this_layer_result)
            else:
                all_result.append(this_layer_result[::-1])

            flag = not flag
            cur_nodes = new_nodes
            
        return all_result


# @lc code=end

