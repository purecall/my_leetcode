#
# @lc app=leetcode.cn id=167 lang=python3
#
# [167] 两数之和 II - 输入有序数组
#

# @lc code=start
class Solution:
    # 双指针法，向中间收缩
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        low, high = 0, len(numbers)-1
        while low < high:
            sum = numbers[low] + numbers[high]
            if sum == target:
                return (low+1, high+1)
            elif sum < target:
                low += 1
            else:
                high -= 1
        return (-1, -1)
# @lc code=end

