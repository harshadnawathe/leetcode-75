from collections import defaultdict
from typing import List


class Solution:
    def maxOperations(self, nums: List[int], k: int) -> int:
        num_index = defaultdict(int)
        ops_count = 0

        for num in nums:
            key = k - num
            if key in num_index:
                if num_index[key] > 1:
                    num_index[key] -= 1
                else:
                    del num_index[key]

                ops_count += 1
            else:
                num_index[num] += 1

        return ops_count
