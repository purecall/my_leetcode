#
# @lc app=leetcode.cn id=151 lang=python3
#
# [151] 翻转字符串里的单词
#

# @lc code=start

# 也可以reversed(s)，再对每个单词reverse一次
# 双端队列也可以
class Solution:
    def reverseWords(self, s: str) -> str:
        return ' '.join(reversed(s.split()))

# @lc code=end