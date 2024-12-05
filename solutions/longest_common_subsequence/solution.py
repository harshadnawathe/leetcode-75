class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        ni, nj = len(text1), len(text2)
        dp = [[0] * (nj + 1) for _ in range(ni + 1)]

        for i in range(ni - 1, -1, -1):
            for j in range(nj - 1, -1, -1):
                if text1[i] == text2[j]:
                    dp[i][j] = 1 + dp[i + 1][j + 1]
                else:
                    dp[i][j] = max(
                        dp[i][j + 1],
                        dp[i + 1][j],
                    )

        return dp[0][0]
