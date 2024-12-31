from typing import List


class Solution:
    def mincostTickets(self, days: List[int], costs: List[int]) -> int:
        travel_days = set(days)
        pass_costs = [(1, costs[0]), (7, costs[1]), (30, costs[2])]
        last_day = days[-1]

        min_cost = [0] * (last_day + 31)
        for day in range(last_day, 0, -1):
            min_cost[day] = (
                min(cost + min_cost[day + days] for days, cost in pass_costs)
                if day in travel_days
                else min_cost[day + 1]
            )

        return min_cost[1]
