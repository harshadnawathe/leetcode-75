from typing import List


class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        result = [0] * len(temperatures)
        stack = [0]

        for today in range(1, len(temperatures)):
            while len(stack) and temperatures[stack[-1]] < temperatures[today]:
                colder_day = stack.pop()
                result[colder_day] = today - colder_day
            stack.append(today)

        return result
