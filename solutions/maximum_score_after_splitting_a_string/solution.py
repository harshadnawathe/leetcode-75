from itertools import starmap, accumulate
from operator import add


class Solution:
    def maxScore(self, s: str) -> int:
        def is_zero(c):
            return c == "0"

        def is_one(c):
            return c == "1"

        return max(
            starmap(
                add,
                zip(
                    list(accumulate(map(is_zero, s[:-1]), add)) + [0],
                    reversed(
                        list(accumulate(map(is_one, reversed(s[1:])), add, initial=0))
                    ),
                ),
            )
        )
