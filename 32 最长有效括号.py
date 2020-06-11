#
# @lc app=leetcode.cn id=32 lang=python3
#
# [32] 最长有效括号
#

# @lc code=start

# 我们首先将 −1-1−1 放入栈顶。

#对于遇到的每个 '(' ，我们将它的下标放入栈中。
# 对于遇到的每个 ')' ，我们弹出栈顶的元素并将当前元素的下标与弹出元素下标作差，
# 得出当前有效括号字符串的长度。通过这种方法，我们继续计算有效子字符串的长度，并最终返回最长有效子字符串的长度。

class Solution:
    def longestValidParentheses(self, s: str) -> int:
        max_ans = 0
        stack = []
        stack.append(-1)
        for i in range(0, len(s)):
            if s[i] == '(':
                stack.append(i)
            else:
                stack.pop()
                if len(stack) == 0:
                    stack.append(i)
                else:
                    max_ans = max(max_ans, i-stack[len(stack)-1])
        return max_ans

# @lc code=end
