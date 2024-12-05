from typing import List


class Solution:
    def maxProfit(self, prices: List[int], fee: int) -> int:
        cash_with_shares = -prices[0]
        cash_without_shares = 0

        for i in range(1, len(prices)):
            cash_with_shares = max(cash_with_shares, cash_without_shares - prices[i])
            cash_without_shares = max(
                cash_without_shares, cash_with_shares + prices[i] - fee
            )

        return cash_without_shares
