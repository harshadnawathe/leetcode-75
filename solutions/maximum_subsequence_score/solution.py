import heapq
from collections import namedtuple
from itertools import starmap
from typing import List


class Solution:
    def maxScore(self, nums1: List[int], nums2: List[int], k: int) -> int:
        Pair = namedtuple("Pair", ["first", "second"])
        pairs = sorted(starmap(Pair, zip(nums1, nums2)), key=lambda p: -p.second)

        print(pairs)

        min_heap = list(map(lambda p: p.first, pairs[:k]))
        heapq.heapify(min_heap)

        print(min_heap)

        top_k_sum = sum(map(lambda p: p.first, pairs[:k]))

        print(top_k_sum)

        max_score = top_k_sum * pairs[k - 1].second

        for i in range(k, len(pairs)):
            top_k_sum += pairs[i].first - heapq.heappop(min_heap)

            heapq.heappush(min_heap, pairs[i].first)

            score = top_k_sum * pairs[i].second

            if max_score < score:
                max_score = score

        return max_score
