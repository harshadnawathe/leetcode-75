from typing import List
from bisect import bisect_left


class Solution:
    def successfulPairs(
        self, spells: List[int], potions: List[int], success: int
    ) -> List[int]:
        potions.sort()

        return [
            len(potions) - bisect_left(potions, (success + s - 1) // s) for s in spells
        ]
