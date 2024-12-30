class Solution:
    MOD = 7 + 10**9

    def countGoodStrings(self, low: int, high: int, zero: int, one: int) -> int:
        dp = [1] + [0] * high

        for n in range(1, high + 1):
            dp[n] = (dp[n - zero] if n - zero >= 0 else 0) + (
                dp[n - one] if n - one >= 0 else 0
            )
            dp[n] %= self.MOD

        return sum(dp[low:]) % self.MOD
