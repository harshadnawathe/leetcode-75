from typing import List


class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort(key=lambda x: x[1])

        count, prev_end = 0, float("-inf")

        for start, end in intervals:
            if start >= prev_end:
                # No overlap
                prev_end = end
            else:
                # Has overlap
                count += 1

        return count
