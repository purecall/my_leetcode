#
# @lc app=leetcode.cn id=455 lang=python3
#
# [455] 分发饼干
#

# @lc code=start


class Solution:
    def findContentChildren(self, g: List[int], s: List[int]) -> int:
        g.sort()
        s.sort()
        idx_g = idx_s = 0
        count = 0

        while idx_s < len(s) and idx_g < len(g):
            if s[idx_s] >= g[idx_g]:
                count += 1
                idx_g += 1
            idx_s += 1  # 满足或不满足，idx_s都要+=1

        return count


# @lc code=end
