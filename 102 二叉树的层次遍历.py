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

# 1. ��ʼʱ������helperֻ�и��ڵ㣬����helper�е�ÿһ���ڵ�
#    ���ν��ڵ��ֵ�������б�new_helper�У������ڵ�����Һ��ӽڵ�(�����)���뵽this_layer_result
# 2. ��new_helper�滻helper������������ֱ��helperΪ��

# (ÿ��while helperѭ����ʼʱ��helper�ж��Ǵ�ŵ�ǰ������нڵ�)
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

