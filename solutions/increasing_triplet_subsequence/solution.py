from typing import List
from math import inf


class Solution:
    def increasingTriplet(self, nums: List[int]) -> bool:
        small = mid = inf

        for num in nums:
            if num <= small:
                small = num
            elif num <= mid:
                mid = num
            else:
                return True

        return False
