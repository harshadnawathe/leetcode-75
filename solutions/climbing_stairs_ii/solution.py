class Solution:
    def climbStairs(self, n: int, costs: list[int]) -> int:

        minCosts = [0, 0, 0]

        for step in range(1, n + 1):
            minCosts[step % 3] = min(
                minCosts[(step - jump) % 3] + costs[step - 1] + jump**2
                for jump in range(1, min(step, 3) + 1)
            )

        return minCosts[n % 3]
