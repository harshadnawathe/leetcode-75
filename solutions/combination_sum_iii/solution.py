from typing import List


class Solution:
    def combinationSum3(self, k: int, n: int) -> List[List[int]]:
        combinations = []

        def backtrack(nums, begin, target):
            if target == 0 and len(nums) == k:
                combinations.append(nums)
                return

            if len(nums) >= k or target < 0:
                return

            for num in range(begin, 10):
                backtrack(nums + [num], num + 1, target - num)

        backtrack([], 1, n)

        return combinations
