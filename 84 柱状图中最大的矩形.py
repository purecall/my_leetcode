#
# @lc app=leetcode.cn id=84 lang=python3
#
# [84] 柱状图中最大的矩形
#

# @lc code=start


class Solution:
    # 维护一个栈(对应高度，单调增加不减的形态)，最初可以压入-1(巧妙)
    # 依次压入新元素，如果这个新元素 >= 栈顶元素，说明栈顶元素的右边界无法确定

    # 如果新元素 < 栈顶元素，栈顶元素的右边界确定，可以计算面积了，并弹出元素
    # 这时再依次和栈顶元素进行比较
    def largestRectangleArea(self, heights: List[int]) -> int:
        size = len(heights)
        res = 0

        stack = []

        for i in range(size):
            while len(stack) > 0 and heights[i] < heights[stack[-1]]:
                # 新元素比栈顶元素小
                cur_height = heights[stack.pop()]

                while len(stack) > 0 and cur_height == heights[stack[-1]]:
                    # 新元素和栈顶元素相同，不断pop
                    stack.pop()

                if len(stack) > 0:
                    cur_width = i - stack[-1]-1
                else:
                    cur_width = i

                res = max(res, cur_height*cur_width)
            stack.append(i)

        # 还剩下一个 单调递增不减 的栈，计算剩下的面积
        while len(stack) > 0:
            cur_height = heights[stack.pop()]
            while len(stack) > 0 and cur_height == heights[stack[-1]]:
                stack.pop()

            if len(stack) > 0:
                # 右边没有比当前height小的了，所以可以从size开始减
                cur_width = size-stack[-1]-1
            else:
                cur_width = size
            res = max(res, cur_height*cur_width)

        return res
            # @lc code=end
