from typing import List


class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        num_delete = 1
        begin = end = 0
        for end in range(len(nums)):
            num_delete -= 1 - nums[end]

            if num_delete < 0:
                num_delete += 1 - nums[begin]
                begin += 1

        return end - begin
