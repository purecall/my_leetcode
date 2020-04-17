#
# @lc app=leetcode.cn id=367 lang=python3
#
# [367] 有效的完全平方数
#

# @lc code=start
class Solution:
    def isPerfectSquare(self, num: int) -> bool:
        if num < 2:
            return True
        
        left,right = 2, num//2
        
        while left <= right:
            mid = left + (right-left)//2
            guess_squared = mid * mid
            if guess_squared == num:
                return True

            if guess_squared > num:
                right = mid -1
            else:
                left = mid +1
        return False
# @lc code=end

