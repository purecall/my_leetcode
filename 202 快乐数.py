#
# @lc app=leetcode.cn id=202 lang=python3
#
# [202] 快乐数
#

# @lc code=start
# 可能会走出一个循环，4→16→37→58→89→145→42→20→4
# 所以用一个set()来检测是否已经出现过
class Solution:
    def isHappy(self, n: int) -> bool:
        def get_next(n):
            total_sum = 0
            while n > 0:
                n, digit = divmod(n, 10)
                total_sum += digit*digit
            return total_sum
        
        seen = set()
        while n!=1 and n not in seen:
            seen.add(n)
            n = get_next(n)
        
        return n==1
            
# @lc code=end

