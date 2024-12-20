class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        m, n = len(text1), len(text2)
        dp = [[0] * (n + 1) for _ in range(m + 1)]

        for i in reversed(range(m)):
            for j in reversed(range(n)):
                dp[i][j] = (
                    1 + dp[i + 1][j + 1]
                    if text1[i] == text2[j]
                    else max(dp[i + 1][j], dp[i][j + 1])
                )

        return dp[0][0]
