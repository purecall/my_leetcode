#
# @lc app=leetcode.cn id=14 lang=python3
#
# [14] 最长公共前缀
#

# @lc code=start
class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if not len(strs):
            return ""
        
        ans = strs[0] # 默认第一个就是ans, 然后不断裁剪
        for i in range(1, len(strs)):
            j = 0
            min_len = min(len(ans), len(strs[i]))
            while j < min_len:
                if ans[j] != strs[i][j]:
                    break
                j += 1
            ans = ans[0:j]
            if not ans:
                return ""
        return ans 

# @lc code=end

