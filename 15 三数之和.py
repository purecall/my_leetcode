# 1. 先将nums排序，复杂度为O(nlogn)
# 2. 基本思路，固定最左(最小)的数字k，若 nums[k] > 0 则break，所以k一直在nums[k]<0的范围内，进行遍历
# 3. 可以得知，如果nums[k] == nums[k+1]，那么可以跳过这个k+1，必定是重复的

# 4. 再设置双指针i j，分别位于(k,len(nums))两端，当i<j时计算三者之和
# 5. 双指针移动规则，如果 sum > 0，则 j -= 1 并跳过重复；如果 sum < 0，则 i += 1 并跳过重复
#    注：比如i,j一开始在两端，分别为最大和最小，这时候，问题转换为求nums[i]...nums[j]这段中，nums[i]+nums[j]==sum的两个值
#        # 为什么可以这样从两边往中间移动？
#        # 可以认为，我们先选了最大的nums[j]，这时，就算是nums[i]和它配对，也无法满足条件，偏大，所以nums[j]是可以从这个备选序列中剔除的，所以可以j -= 1
# 6. 如果 sum == 0，则 同时 i += 1和 j -= 1并跳过重复

# 时间复杂度O(n^2)：固定指针k循环复杂度为O(n)，双指针i,j复杂度为O(n)
# 空间复杂度O(1)：指针使用常量大小的空间

class Solution:
    def threeSum(self, nums):
        nums.sort()
        result, k = [], 0
        for k in range(0, len(nums)-2):  # length >= 3
            if nums[k] > 0:
                break  # because j > i > k
            if k > 0 and nums[k] == nums[k-1]:
                continue  # skip the same nums[k]
            i, j = k+1, len(nums)-1

            while i < j:  # double pointer
                sum = nums[k] + nums[i] + nums[j]
                if sum < 0:
                    i += 1
                    while i < j and nums[i] == nums[i-1]:
                        i += 1
                elif sum > 0:
                    j -= 1
                    while i < j and nums[j] == nums[j+1]:
                        j -= 1
                else:  # sum == 0
                    result.append([nums[k], nums[i], nums[j]])
                    i += 1
                    j -= 1
                    while i < j and nums[i] == nums[i-1]:
                        i += 1
                    while i < j and nums[j] == nums[j+1]:
                        j -= 1
        return result


# 解法2 哈希表 待做