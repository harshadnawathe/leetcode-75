from typing import List
from heapq import heapify, heappush, heappop


class Solution:
    def totalCost(self, costs: List[int], k: int, candidates: int) -> int:
        left, right = 0, len(costs)
        left_heap, right_heap = [], []

        for _ in range(candidates):
            if left < right:
                left_heap.append(costs[left])
                left += 1
            else:
                break

        heapify(left_heap)

        for _ in range(candidates):
            if left < right:
                right -= 1
                right_heap.append(costs[right])
            else:
                break

        heapify(right_heap)

        total_cost = 0
        rounds = 0

        while rounds < k and right_heap and left_heap:
            rounds += 1

            if right_heap[0] < left_heap[0]:
                total_cost += heappop(right_heap)
                if left < right:
                    right -= 1
                    heappush(right_heap, costs[right])
            else:
                total_cost += heappop(left_heap)
                if left < right:
                    heappush(left_heap, costs[left])
                    left += 1

        while right_heap and rounds < k:
            rounds += 1
            total_cost += heappop(right_heap)
            if left < right:
                right -= 1
                heappush(right_heap, costs[right])

        while left_heap and rounds < k:
            rounds += 1
            total_cost += heappop(left_heap)
            if left < right:
                heappush(left_heap, costs[left])
                left += 1

        return total_cost
