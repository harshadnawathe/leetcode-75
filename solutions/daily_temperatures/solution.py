from typing import List


class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        result = [0] * len(temperatures)
        stack = []

        for today, temperature in enumerate(temperatures):
            while stack and temperatures[stack[-1]] < temperature:
                colder_day = stack.pop()
                result[colder_day] = today - colder_day
            stack.append(today)

        return result
