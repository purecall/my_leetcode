#
# @lc app=leetcode.cn id=37 lang=python3
#
# [37] 解数独
#

# @lc code=start
class Solution:
    def solveSudoku(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        self.backtrack(board, 0, 0)
        return board

    def backtrack(self, board, i, j):
        m, n = 9, 9
        # 到达第n列，越界，换到下一行第0列重新开始
        if j == n:
            return self.backtrack(board, i+1, 0)
        # 到达第m行，说明找到了可行解，触发base case
        if i == m:
            return True
        # 如果有预设数字，不需要穷举
        if board[i][j] != '.':
            return self.backtrack(board, i, j+1)
        
        for val in range(1, 10):
            # 如果遇到不合法的数字，就跳过
            if not self.isValid(board, i, j, str(val)):
                continue
                
            # 添加选择
            board[i][j] = str(val)
            # 如果找到一个可行解，立即结束
            if self.backtrack(board, i, j+1):
                return True
            # 撤回选择
            board[i][j] = '.'
        # 穷举完 1-9,依然没有找到可行解，此路不通
        return False
    
    def isValid(self, board, row, col, val):
        for i in range(9):
            # 判断行是否存在重复
            if board[row][i] == val:
                return False
            if board[i][col] == val:
                return False
            # 判断3x3方框中是否存在重复
            if board[row//3*3 + i//3][col//3*3 + i%3] == val:
                return False
        return True
                
# @lc code=end

