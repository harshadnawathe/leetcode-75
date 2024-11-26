from typing import List


class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        rows, cols = len(grid), len(grid[0])
        rotten = [(r, c) for r in range(rows) for c in range(cols) if grid[r][c] == 2]
        fresh_count = sum(grid[r][c] == 1 for r in range(rows) for c in range(cols))

        if not fresh_count:
            return 0

        minutes = 0
        while rotten:
            next_rotten = []

            for row, col in rotten:
                for next_row, next_col in [
                    (row + 1, col),
                    (row - 1, col),
                    (row, col + 1),
                    (row, col - 1),
                ]:
                    if (
                        0 <= next_row < rows
                        and 0 <= next_col < cols
                        and grid[next_row][next_col] == 1
                    ):
                        grid[next_row][next_col] = 2
                        next_rotten.append((next_row, next_col))

            fresh_count -= len(next_rotten)
            minutes += 1
            rotten = next_rotten

        return -1 if fresh_count else minutes - 1
