class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        m, n = len(word1), len(word2)
        md = [
            [r + c if r == 0 or c == 0 else 0 for c in range(n + 1)]
            for r in range(m + 1)
        ]

        for r in range(1, m + 1):
            for c in range(1, n + 1):
                if word1[r - 1] == word2[c - 1]:
                    md[r][c] = md[r - 1][c - 1]
                else:
                    md[r][c] = 1 + min(md[r - 1][c - 1], md[r][c - 1], md[r - 1][c])

        return md[-1][-1]
