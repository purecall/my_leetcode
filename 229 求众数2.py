#
# @lc app=leetcode.cn id=229 lang=python3
#
# [229] 求众数 II
#

# @lc code=start
class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        from collections import Counter
        counts = Counter(nums)
        count = len(nums) // 3

        ans = []
        for k, v in counts.items():
            if v > count:
                ans.append(k)
        return ans
# @lc code=end


class Solution1:
    # 稍微有点细节没想明白...不过大概理解了
    def majorityElement(self, nums: List[int]) -> List[int]:
        if not nums:
            return []
        # 两个有希望的数
        cand1 = nums[0]
        cand2 = nums[0]
        count1 = count2 = 0

        for num in nums:
            if cand1 == num:
                count1 += 1
                continue
            if cand2 == num:
                count2 += 1
                continue
            if count1 == 0:
                cand1 = num
                count1 += 1
                continue
            if count2 == 0:
                cand2 = num
                count2 += 1
                continue
            # cand1和cand2和num都不同，三者抵消
            # 抵消的理由（柱状图）：https://leetcode-cn.com/problems/majority-element-ii/solution/cong-zhu-xing-tu-jiao-chao-ji-su-li-jie-wei-shi-ya/
            count1 -= 1
            count2 -= 1
        
        # 检查这两个有希望的数是否满足条件
        count1 = 0
        count2 = 0
        for num in nums:
            if cand1 == num:
                count1 += 1
            elif cand2 == num:
                count2 += 1
        
        res = []
        if count1 > len(nums)//3:
            res.append(cand1)
        if count2 > len(nums)//3:
            res.append(cand2)
        return res
