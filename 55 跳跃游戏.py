class Solution:
    def canJump(self, nums) :
        k = 0
        for idx, num in enumerate(nums):
            if idx > k:
                return False
            if k >= len(nums):
                return True

            k = max(k, idx+num)
        return True 