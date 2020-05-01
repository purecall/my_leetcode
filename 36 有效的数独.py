#
# @lc app=leetcode.cn id=36 lang=python3
#
# [36] 有效的数独
#

# @lc code=start
class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        def isValid(lst):
            nums = list(filter(lambda x: x!='.', lst))
            return len(nums)==len(set(nums))

        for row in board: # 9行
            if not isValid(row):
                return False
        
        for col in zip(*board): # 9列 -> zip 将可迭代对象重新打包
            if not isValid(col):
                return False

        for row in range(3): # 判断3*3
            for col in range(3):
                tmp = [board[i][j] for i in range(row*3, row*3+3) for j in range(col*3, col*3 + 3)]
                if not isValid(tmp):
                    return False
                    
        return True
# @lc code=end

