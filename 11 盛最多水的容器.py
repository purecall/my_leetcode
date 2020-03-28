class Solution:
    # 复杂度为O(n^2),暴力计算所有组合求解
    def maxArea(self, height: List[int]) -> int:
        max_area = 0
        for i in range(len(height)):
            for j in range(i+1, len(height)):
                min_height = min(height[i], height[j])
                cur_area = min_height*(j-i)
                max_area = max(max_area, cur_area)
        return max_area

class Solution1:
    # 复杂度为O(n)，双指针往中间收敛，哪个height小，就让这个指针移动
    # 因为往中间收敛时，(j-i)必定减小，所以试图寻求更大的height
    # 两个height实质上是等价关系，所以显然移动小的height
    def maxArea(self, height: List[int]) -> int:
        max_area = 0
        i, j = 0, len(height)-1
        while i != j:
            min_height = min(height[i], height[j])
            cur_area = (j-i)*min_height
            max_area = max(max_area, cur_area)
            if height[i] < height[j]:
                i += 1
            else:
                j -= 1
        return max_area

