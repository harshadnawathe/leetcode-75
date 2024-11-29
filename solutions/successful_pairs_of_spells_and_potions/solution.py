from typing import List
from bisect import bisect_left


class Solution:
    def successfulPairs(
        self, spells: List[int], potions: List[int], success: int
    ) -> List[int]:
        potions = sorted(potions)

        result = [0] * len(spells)

        for i, spell in enumerate(spells):
            result[i] = len(potions) - bisect_left(
                potions, success, key=lambda potion: potion * spell
            )

        return result
