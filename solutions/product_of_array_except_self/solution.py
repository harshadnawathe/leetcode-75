from typing import List


class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        result = [1] * n
        pre, post = 1, 1

        for i in range(n):
            result[i] *= pre
            pre *= nums[i]
            result[n - i - 1] *= post
            post *= nums[n - i - 1]

        return result
