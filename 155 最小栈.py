#
# @lc app=leetcode.cn id=155 lang=python3
#
# [155] 最小栈
#

# @lc code=start

# 数据栈与辅助栈同步(大小也相同)
# 每次在数据栈中push，都会在辅助栈push(当前最小值)
# pop时，两个栈都pop(注意data==[]的情况)

class MinStack:
    def __init__(self):
        """
        initialize your data structure here.
        """
        self.data = []   # 数据栈
        self.helper = []  # 辅助栈

    def push(self, x: int) -> None:
        self.data.append(x)
        if len(self.helper) == 0 or x <= self.helper[-1]:
            self.helper.append(x)
        else:
            self.helper.append(self.helper[-1])

    def pop(self) -> None:
        if self.data:
            self.helper.pop()
            return self.data.pop()

    def top(self) -> int:
        if self.data:
            return self.data[-1]

    def getMin(self) -> int:
        if self.helper:
            return self.helper[-1]


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(x)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()
# @lc code=end


# 解法2: 不使用辅助栈，封装存入stack的数据为pair (x,cur_min)
class MinStack1:
    def __init__(self):
        """
        initialize your data structure here.
        """
        self.data = []  # 数据成员 (x,min) 每次存一个`pair`

    def push(self, x: int) -> None:
        if self.data:  # data非空
            if x < (self.data[-1])[1]:  # 当前记录的整个栈的min
                self.data.append((x, x))
            else:
                self.data.append((x, (self.data[-1])[1]))
        else:  # data为空
            self.data.append((x, x))

    def pop(self) -> None:
        if self.data:
            self.data.pop()

    def top(self) -> int:
        if self.data:
            return (self.data[-1])[0]

    def getMin(self) -> int:
        if self.data:
            return (self.data[-1])[1]