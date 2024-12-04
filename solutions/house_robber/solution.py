from typing import List


class Solution:
    def rob(self, nums: List[int]) -> int:
        n1, n2 = 0, 0
        for i in range(len(nums) - 1, -1, -1):
            n1, n2 = max(nums[i] + n2, n1), n1

        return n1
