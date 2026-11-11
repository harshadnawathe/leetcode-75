class Solution:
    def minimumCost(self, cost1: int, cost2: int, costBoth: int, need1: int, need2: int) -> int:
        min_items_purchased = min(need1, need2)
        return min(
            need1 *cost1 + need2 * cost2,
            costBoth * max(need1, need2),
            costBoth * min_items_purchased + cost1 * (need1 - min_items_purchased) + cost2 * (need2 - min_items_purchased)
        )

