from typing import List


class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        def visit(city: int):
            if not isConnected[city][city]:
                return

            isConnected[city][city] = 0

            for next_city, can_visit in enumerate(isConnected[city]):
                if can_visit:
                    visit(next_city)

        num_provinces = 0
        for city in range(len(isConnected)):
            if isConnected[city][city]:
                visit(city)
                num_provinces += 1

        return num_provinces
