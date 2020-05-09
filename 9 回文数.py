#
# @lc app=leetcode.cn id=9 lang=python3
#
# [9] 回文数
#

# @lc code=start
# 但好像还是这个版本效率更高
class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x < 0:
            return False 
        if x == 0:
            return True
        xx = x
        y = 0
        while xx != 0:
            y *= 10
            y += (xx % 10)
            xx //= 10
        
        return x == y
# @lc code=end


# 只反转一半
class Solution2:
    def isPalindrome(self, x: int) -> bool:
        if x < 0:
            return False 
        if x == 0:
            return True
        
        from math import log
        length = int(log(x, 10)) + 1
        reversed_x = 0
        for _ in range(length//2):
            # x自身会//=10，不断变小
            reversed_x *= 10
            reversed_x += (x % 10)
            x //= 10
        
        if length % 2 == 0:
            return x == reversed_x
        else:
            return x // 10 == reversed_x 
