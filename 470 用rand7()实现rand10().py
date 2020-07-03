#
# @lc app=leetcode.cn id=470 lang=python3
#
# [470] 用 Rand7() 实现 Rand10()
#

# @lc code=start
# The rand7() API is already defined for you.
# def rand7():
# @return a random integer in the range 1 to 7

class Solution:
    def rand10(self):
        """
        :rtype: int
        """
        # a = rand7()     => 1...7
        # b = (rand7()-1) => 0...6  * 7
        # a+b即可均匀生成1-49的数

        """ 舍弃的太多了
        num = rand7() + (rand7()-1)*7
        while num > 10:
            num = rand7() + (rand7()-1)*7
        return num
        """

        # 舍弃了9个，不再进一步优化了...
        num = rand7() + (rand7()-1)*7
        while num > 40:
            num = rand7() + (rand7()-1)*7
        return 1 + num % 10
        # 1...40  num % 10生成4组0-9，+1即可

        
# @lc code=end

