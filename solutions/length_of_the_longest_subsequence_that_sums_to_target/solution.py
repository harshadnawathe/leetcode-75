from typing import List


class Solution:
    def lengthOfLongestSubsequence(self, nums: List[int], target: int) -> int:
        cache = [[-1] * (target + 1) for _ in range(len(nums) + 1)]

        def max_len(pos, sum):
            if sum > target:
                return -float("inf")

            if sum == target:
                return 0

            if pos == len(nums):
                return -float("inf")

            if cache[pos][sum] != -1:
                return cache[pos][sum]

            result = max(
                1 + max_len(pos + 1, sum + nums[pos]),
                max_len(pos + 1, sum),
            )

            cache[pos][sum] = result

            return result

        result = max_len(0, 0)

        if result == -float("inf"):
            return -1

        return int(result)
