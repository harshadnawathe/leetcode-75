from typing import List


class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        max_diff = diff = 0

        for i in range(len(nums) - k):
            diff += nums[i + k] - nums[i]
            if max_diff < diff:
                max_diff = diff

        return (sum(nums[:k]) + max_diff) / k
