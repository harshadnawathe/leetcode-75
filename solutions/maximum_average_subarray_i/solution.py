from typing import List
from math import inf


class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        max_avg = -inf
        begin = 0
        sum = 0

        for curr, num in enumerate(nums):
            win_size = curr - begin + 1
            sum += num

            if win_size == k:
                max_avg = max(max_avg, sum / k)

                # Shift window
                sum -= nums[begin]
                begin += 1

        return max_avg
