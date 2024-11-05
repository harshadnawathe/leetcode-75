from typing import List


class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        max_candies = max(candies)

        return [
            all(map(lambda _: candy + extraCandies >= max_candies, candies))
            for candy in candies
        ]
