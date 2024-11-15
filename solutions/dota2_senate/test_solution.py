from solutions.dota2_senate.solution import Solution

tests = [
    ("Example 1", {"args": {"senate": "RD"}, "expected": "Radiant"}),
    ("Example 2", {"args": {"senate": "RDD"}, "expected": "Dire"}),
]


def test_dota2_senate(args, expected):
    solution = Solution()

    assert solution.predictPartyVictory(**args) == expected
