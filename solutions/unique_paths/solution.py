class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        dp = [1] * n

        for _ in range(1, m):
            for c in range(1, n):
                dp[c] = dp[c - 1] + dp[c]

        return dp[-1]
