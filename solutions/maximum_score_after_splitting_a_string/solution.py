from itertools import accumulate


class Solution:
    def maxScore(self, s: str) -> int:
        zeros = list(accumulate(1 if c == "0" else 0 for c in s[:-1]))

        ones = list(accumulate(1 if c == "1" else 0 for c in reversed(s[1:])))
        ones.reverse()

        return max(z + o for z, o in zip(zeros, ones))
