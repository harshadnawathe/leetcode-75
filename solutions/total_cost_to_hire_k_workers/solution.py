from typing import List
from heapq import heapify, heappush, heappop


class Solution:
    def totalCost(self, costs: List[int], k: int, candidates: int) -> int:
        left = min(candidates, len(costs))
        right = max(candidates, len(costs) - candidates)

        left_heap = costs[:left]
        heapify(left_heap)

        right_heap = costs[right:]
        heapify(right_heap)

        total_cost = 0
        for _ in range(k):
            if not right_heap or (left_heap and left_heap[0] <= right_heap[0]):
                total_cost += heappop(left_heap)
                if left < right:
                    heappush(left_heap, costs[left])
                    left += 1
            else:
                total_cost += heappop(right_heap)
                if left < right:
                    right -= 1
                    heappush(right_heap, costs[right])

        return total_cost
