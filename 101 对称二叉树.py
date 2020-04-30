# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def isSymmetric(self, root: TreeNode) -> bool:
        def helper(left: TreeNode, right: TreeNode):
            if left == None and right == None:
                return True
            if left == None or right == None: # 仅一个为None
                return False
            if left.val != right.val:
                return False
            
            # 判断左子树的左子树和右子树的右子树是否对称
            # 以及左子树的右子树和右子树的左子树是否对称
            return helper(left.left, right.right) and helper(left.right, right.left)

        return (root == None) or helper(root.left, root.right)
    
