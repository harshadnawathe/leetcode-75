from typing import List


class Solution:
    def maxArea(self, height: List[int]) -> int:
        left, right = 0, len(height) - 1
        result = 0

        while left < right:
            left_height, right_height = height[left], height[right]
            area = 0
            if left_height < right_height:
                area = left_height * (right - left)
                left += 1
            else:
                area = right_height * (right - left)
                right -= 1

            result = max(result, area)

        return result
