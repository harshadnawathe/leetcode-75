from typing import List


class Solution:
    def rob(self, nums: List[int]) -> int:
        n1, n2 = 0, 0
        for num in reversed(nums):
            n1, n2 = max(num + n2, n1), n1

        return n1
