from typing import List


class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        begin = end = 0
        for end, num in enumerate(nums):
            k -= 1 - num
            if k < 0:
                k += 1 - nums[begin]
                begin += 1

        return end - begin + 1
