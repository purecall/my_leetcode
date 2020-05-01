#
# @lc app=leetcode.cn id=51 lang=python3
#
# [51] N皇后
#

# @lc code=start

# 回溯法
class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        board = [['.']*n for _ in range(n)] # 初始化二维棋盘
        res = []

        # col 竖行 row 横行
        def backtrack(board, row):
            """
            if 满足条件
                res.append(路径)
                return
            """
            if row == len(board):
                tmp_list = []
                for e_row in board:
                    tmp = ''.join(e_row)
                    tmp_list.append(tmp)
                res.append(tmp_list)
                return 
            """
            for 选择 in 选择列表:
                做选择
                backtrack(路径, 选择列表)
                撤销选择
            """
            for col in range(len(board[0])):
                if not isValid(board, row, col):
                    continue
                board[row][col] = 'Q'
                backtrack(board, row+1)
                board[row][col] = '.'
            
        def isValid(board, row, col):
            n = len(board)
            # 检查列是否有皇后互相冲突
            for i in range(n):
                if board[i][col] == 'Q':
                    return False
            
            # 检查右上方是否有皇后互相冲突
            r_row, r_col = row, col
            while r_row > 0 and r_col < n-1:
                r_row -= 1
                r_col += 1
                if board[r_row][r_col] == 'Q':
                    return False
            
            # 检查左上方是否有皇后互相冲突
            l_row, l_col = row, col
            while l_row > 0 and l_col > 0:
                l_row -= 1
                l_col -= 1
                if board[l_row][l_col] == 'Q':
                    return False
            
            return True
        
        backtrack(board, 0)
        return res
# @lc code=end

