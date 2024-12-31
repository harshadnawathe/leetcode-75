from typing import List


class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        dp = [0] + [amount + 1] * (amount)

        for curr_amount in range(1, amount + 1):
            for coin in coins:
                if coin <= curr_amount:
                    dp[curr_amount] = min(dp[curr_amount], dp[curr_amount - coin] + 1)

        return dp[amount] if dp[amount] <= amount else -1
