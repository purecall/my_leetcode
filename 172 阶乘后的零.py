#
# @lc app=leetcode.cn id=172 lang=python3
#
# [172] 阶乘后的零
#

# @lc code=start
# 6! = 6 5 4 3 2 1 = (3*2) 5 (2*2) 3 2 1
# 出现5的频率远高于2，所以只要考虑5的个数
# 5的倍数 +1   25的倍数 +2    125的倍数 +3

class Solution:
    def trailingZeroes(self, n: int) -> int:
        count = 0
        while n:
            n //= 5
            count += n
        return count
        

# @lc code=end