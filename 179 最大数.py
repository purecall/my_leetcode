#
# @lc app=leetcode.cn id=179 lang=python3
#
# [179] 最大数
#

# @lc code=start
class Solution:
    # python3 自定义排序函数，key = cmp_to_key(lambda x, y: int(y + x) - int(x + y))
    def largestNumber(self, nums: List[int]) -> str:
        if not nums:
            return ''
        nums = map(str, nums)

        from functools import cmp_to_key
        # python2 cmp(x+y,y+x)直接字符串比较即可，python3必须这么写
        cmp_key = cmp_to_key(lambda x,y : int(y+x) - int(x+y))
        
        res = ''.join(sorted(nums,key=cmp_key)).lstrip('0')
        # '000'
        return res or '0'
# @lc code=end

