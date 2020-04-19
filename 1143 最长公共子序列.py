#
# @lc app=leetcode.cn id=1143 lang=python3
#
# [1143] 最长公共子序列
#

# @lc code=start


class Solution:
    # S{s1,s2,s3....si} T{t1,t2,t3....tj}
    # 子问题划分
    # 1. 如果S的最后一位等于T的最后一位，那么最大子序列就是
    #    {s1,s2,s3...si-1}和{t1,t2,t3...tj-1} 的最大子序列 +1

    # 2. 如果S的最后一位不等于T的最后一位，那么最大子序列就是
    #    {s1,s2,s3..si}和 {t1,t2,t3...tj-1} 最大子序列
    #    {s1,s2,s3...si-1}和{t1,t2,t3...tj} 最大子序列
    #    中的较大者

    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        # m+1行 n+1列
        m = len(text1)
        n = len(text2)
        dp = [[0]*(n+1) for _ in range(m+1)]

        for i in range(1, m+1):
            for j in range(1, n+1):
                if text1[i-1] == text2[j-1]:
                    dp[i][j] = dp[i-1][j-1]+1
                else:
                    # 考虑 dp table 当前位置和其左上角的位置
                    # 同时多出来一个字符
                    # 要么能被当前位置上面一个字符利用
                    # 要么能被当前位置左边一个位置利用
                    # 所以 max(dp[i-1][j], dp[i][j-1])
                    # 即为这两个位置的最大值
                    dp[i][j] = max(dp[i-1][j], dp[i][j-1])
        return dp[-1][-1]
        # @lc code=end
