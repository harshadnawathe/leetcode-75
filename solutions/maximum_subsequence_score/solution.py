from heapq import heapify, heappop, heappush
from typing import List


class Solution:
    def maxScore(self, nums1: List[int], nums2: List[int], k: int) -> int:
        pairs = sorted(zip(nums1, nums2), key=lambda p: -p[1])

        min_heap = [num1 for num1, _ in pairs[:k]]
        heapify(min_heap)

        top_k_sum = sum(min_heap)

        max_score = top_k_sum * pairs[k - 1][1]

        for num1, num2 in pairs[k:]:
            top_k_sum += num1 - heappop(min_heap)
            heappush(min_heap, num1)

            max_score = max(max_score, top_k_sum * num2)

        return max_score
