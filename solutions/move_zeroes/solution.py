from typing import List


class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        i, j = 0, 0
        while j < len(nums):
            # Skip all zero elements
            while j < len(nums) and not nums[j]:
                j += 1

            # Swap all non-zero elements
            while j < len(nums) and nums[j]:
                nums[i], nums[j] = nums[j], nums[i]
                i += 1
                j += 1
