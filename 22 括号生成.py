#
# @lc app=leetcode.cn id=22 lang=python3
#
# [22] 括号生成
#

# @lc code=start


# 定义递归函数，传参 当前形成括号字符串，左括号剩余数，右括号剩余数
# 如果左右括号都用完了，结果加到总结果列表中
# 如果左括号还有，那么先用一个左括号，再递归试试
# 如果右括号数量比左括号多，那么右括号也可以先用一个，再递归试试
class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        res = []

        def helper(s, l, r):
            if not l and not r:
                res.append(s)
            if 0 <= l:
                helper(s+'(', l-1, r)
            if r > l:
                helper(s+')', l, r-1)
        
        helper('', n, n)
        return res
# @lc code=end
