from typing import List
from operator import mul
from itertools import accumulate


class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        left_product = list(accumulate(nums, mul))
        right_product = list(accumulate(nums[::-1], mul))[::-1]

        return [
            (left_product[i - 1] if i > 0 else 1)
            * (right_product[i + 1] if i < len(nums) - 1 else 1)
            for i in range(len(nums))
        ]
