class Solution:
    def numTilings(self, n: int) -> int:
        a, b, c = 1, 1, 0
        for _ in range(1, n):
            a, b, c = b, a + b + 2 * c, b + c
        return b % 1000000007
