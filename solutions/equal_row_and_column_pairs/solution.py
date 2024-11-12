from typing import List


class Solution:
    def equalPairs(self, grid: List[List[int]]) -> int:
        row_hashes = [hash(str(x)) for x in grid]
        col_hashes = [hash(str([x[i] for x in grid])) for i in range(len(grid))]

        count = 0
        for row_hash in row_hashes:
            for col_hash in col_hashes:
                count += row_hash == col_hash

        return count
