from typing import List
from itertools import accumulate
from operator import add


class Solution:
    def largestAltitude(self, gain: List[int]) -> int:
        return max(accumulate(gain, add, initial=0))
