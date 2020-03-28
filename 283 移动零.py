class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        # 一层循环依次扫过，把非零值依次往前移动
        current_idx = 0
        for num in nums:
            if num != 0:
                nums[current_idx] = num
                current_idx += 1

        # 再把最后给zero_num个元素置零
        for i in range(current_idx, len(nums)):
            nums[i] = 0


class Solution1:
    def moveZeroes(self, nums: List[int]) -> None:
        zero_position = 0  # 记录最前面的零值的位置
        for i in range(len(nums)):
            if nums[i] != 0:
                nums[i], nums[zero_position] = nums[zero_position], nums[i]
                zero_position += 1