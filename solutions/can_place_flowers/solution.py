from typing import List


class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        num_placed = 0

        for i in range(len(flowerbed)):
            if self._can_place_flower(flowerbed, i):
                flowerbed[i] = 1
                num_placed += 1
                if num_placed >= n:
                    return True

        return num_placed >= n

    def _can_place_flower(self, flowerbed: List[int], pos: int) -> bool:
        if flowerbed[pos] == 0:
            if self._is_empty(flowerbed, pos - 1) and self._is_empty(
                flowerbed, pos + 1
            ):
                return True

        return False

    def _is_empty(self, flowerbed: List[int], pos: int) -> bool:
        if pos == -1 or pos == len(flowerbed):
            return True
        else:
            return flowerbed[pos] == 0
