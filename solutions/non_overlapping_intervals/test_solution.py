from solutions.non_overlapping_intervals.solution import Solution

tests = [
    (
        "Example 1",
        {"args": {"intervals": [[1, 2], [2, 3], [3, 4], [1, 3]]}, "expected": 1},
    ),
    (
        "Example 2",
        {"args": {"intervals": [[1, 2], [1, 2], [1, 2]]}, "expected": 2},
    ),
    (
        "Example 3",
        {"args": {"intervals": [[1, 2], [2, 3]]}, "expected": 0},
    ),
]


def test_non_overlapping_intervals(args, expected):
    solution = Solution()

    assert solution.eraseOverlapIntervals(**args) == expected
