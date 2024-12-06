from typing import List


class Solution:
    def findMinArrowShots(self, points: List[List[int]]) -> int:
        points.sort(key=lambda x: x[1])

        count, prev_end = 0, float("-inf")

        for start, end in points:
            if start > prev_end:
                count += 1
                prev_end = end

        return count
