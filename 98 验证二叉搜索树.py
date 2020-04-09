#
# @lc app=leetcode.cn id=98 lang=python3
#
# [98] 验证二叉搜索树
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

# 用yield，注意这里的写法，一共要三处yield
# 而不是只遍历左(右)子树只在中间yield root.val
def yieldTree(root: TreeNode):
    if not root:
        return 
    for i in yieldTree(root.left):
        yield i
    yield root.val
    for i in yieldTree(root.right):
            yield i

class Solution:            
    def isValidBST(self, root: TreeNode) -> bool:
        if root is None:
            return True
        num = -2147483649
        for i in yieldTree(root):
            if num >= i:
                return False
            num = i
        return True

# @lc code=end


'''
class Solution:
    def isValidBST(self, root: TreeNode) -> bool:
        # 空间复杂度较高，先中序遍历为数组，再判断该数组是否严格递增(if all)
        res = []

        def helper(root):
            if not root:
                return
            helper(root.left)
            res.append(root.val)
            helper(root.right)
        helper(root)
        
        if all([res[i] < res[i+1] for i in range(len(res)-1)]):
            return True
        return False
'''
