from solutions.is_subsequence.solution import Solution

tests = [
    ("Example 1", {"args": {"s": "abc", "t": "ahbgdc"}, "expected": True}),
    ("Example 2", {"args": {"s": "axc", "t": "ahbgdc"}, "expected": False}),
]


def test_is_subsequence(args, expected):
    solution = Solution()

    assert solution.isSubsequence(**args) == expected
