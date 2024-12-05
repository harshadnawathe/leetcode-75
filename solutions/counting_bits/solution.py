from typing import List


class Solution:
    def countBits(self, n: int) -> List[int]:
        bit_count = [0] * (n + 1)
        for i in range(1, n + 1):
            bit_count[i] = 1 + bit_count[i & (i - 1)]

        return bit_count
